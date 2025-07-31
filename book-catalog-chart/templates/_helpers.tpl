{{/* Generate a fullname */}}
{{- define "book-catalog.fullname" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}