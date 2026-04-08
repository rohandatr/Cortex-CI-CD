resource "aws_s3_bucket" "bad_bucket" {
  bucket = "cortex-demo-bucket"
  acl    = "public-read"   #  misconfiguration
}