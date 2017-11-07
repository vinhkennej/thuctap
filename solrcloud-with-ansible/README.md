# Deloy an external SolrCloud Cluster with Ansible 

## Install Zookeeper
	ansible-playbook -i hosts site.yml --tags "setup_zoo"

## Install Solr
	ansible-playbook -i hosts site.yml --tags "setup_solr"

## Restart Zookeeper
	ansible-playbook -i hosts site.yml --tags "restart_zoo"

## Create a new Collection in Solr
	ansible-playbook -i hosts site.yml --tags "create_collection" --limit servers[0]

## Create a new Collection using HTTP
- Uploading configuration set to Zookeeper

		ansible-playbook -i hosts site.yml --tags "upload_configset" --limit servers[0]

- Create collection

		ansible-playbook -i hosts site.yml --tags "create_collection_http" --limit servers[0]

## Upload Database

	ansible-playbook -i hosts site.yml --tags "upload_db" --limit servers[0]

## Reload a Collection

	ansible-playbook -i hosts site.yml --tags "reload_collection" --limit servers[0]

## Delete a Collection

	ansible-playbook -i hosts site.yml --tags "delete_collection" --limit servers[0]
