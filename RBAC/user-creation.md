  878  k config view
  880  k config get-contexts
  881  openssl genrsa -out gbhure.key 2048

CA Signing request
  900  openssl req -new -key gbhure.key -out gbhure.csr -subj "/CN=gbhure/O=dev/O=example.org"

Generate certificate
  918  openssl x509 -req -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -days 730  -in gbhure.csr -out gbhure.crt

OR for kind cluster
docker ps
7456b9660e67   kindest/node:v1.31.0   "/usr/local/bin/entr…"   4 days ago   Up 2 minutes   127.0.0.1:35123->6443/tcp   kind-control-plane
docker cp 7456b9660e67:/etc/kubernetes/pki/ca.key /root/.kube/
docker cp 7456b9660e67:/etc/kubernetes/pki/ca.crt /root/.kube/
  918  openssl x509 -req -CA /root/.kube/ca.crt -CAkey /root/.kube/ca.key -CAcreateserial -days 730  -in gbhure.csr -out gbhure.crt


  920  k config view
  921  k config set-credentials gbhure --client-certificate=gbhure.crt --client-key=gbhure.key
  922  k config view

Add context
$ k config set-context gbhure@dev --cluster=dev --user=gbhure --namespace=default

$ k config view


  945  k config use-context gbhure@dev
  946  k config get-contexts
  947  k config use-context kubernetes-admin@kubernetes
  948  k config get-contexts
  949  k get po
  950  k config use-context gbhure@dev
  951  k get po



cat role.yml 
———
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: testuser
  namespace: default
rules:
  - apiGroups: ["*"]
    resources: ["*"]
    verbs: ["*"]



root@ip-172-31-35-144:/home/ubuntu/kubernetes-demo/rbac# cat rolebinding.yml 
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: testadmbinding
  namespace: default
subjects:
  - kind: User
    name: gbhure
    apiGroup: ""
roleRef:
  kind: Role
  name: testuser
  apiGroup: ""


