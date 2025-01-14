/*
 * faasnap
 *
 * FaaSnap API
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

type Snapshot struct {
	VmId string `json:"vmId"`
	SsId string `json:"ssId,omitempty"`
	SnapshotType string `json:"snapshot_type,omitempty"`
	SnapshotPath string `json:"snapshot_path,omitempty"`
	MemFilePath string `json:"mem_file_path,omitempty"`
	Version string `json:"version,omitempty"`
	RecordRegions bool `json:"record_regions,omitempty"`
	SizeThreshold int32 `json:"size_threshold,omitempty"`
	IntervalThreshold int32 `json:"interval_threshold,omitempty"`
}
