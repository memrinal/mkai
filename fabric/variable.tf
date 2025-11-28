variable "workspace_name" {
  type    = string
  default = "enterprise-dl"
}

variable "capacity_id" {
  type    = string
  default = "3BB1DEAD-7437-4718-AB7A-20787920F2E4" # You can use a data source to fetch this dynamically
}