## To create project:
$ aws configure

`aws_access_key_id` = <aws_access_key_id><br>
`aws_secret_access_key` = <aws_secret_access_key><br>
`region` = us-west-2<br>
`output` = json

$ `pip install chalice`

$ `chalice new-project chalice-demo`

## To deploy project:

$ `chalice deploy`

## To delete project deployment:

$ `chalice delete`

## To run the server in local env:

$ `chalice local`

## Notes
Add dependency files to `chalicelib`<br>
Add layers in `.chalice/config.json`
