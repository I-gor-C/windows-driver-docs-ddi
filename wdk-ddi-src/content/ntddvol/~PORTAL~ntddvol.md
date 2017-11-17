# Declarations in the ntddvol header
This header Ntddvol contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [VOLUME_GET_BC_PROPERTIES_OUTPUT structure](ns-ntddvol--volume-get-bc-properties-output.md) | TBD |
| [VOLUME_SET_GPT_ATTRIBUTES_INFORMATION structure](ns-ntddvol--volume-set-gpt-attributes-information.md) | TBD |
| [VOLUME_ALLOCATION_HINT_INPUT structure](ns-ntddvol--volume-allocation-hint-input.md) | TBD |
| [VOLUME_FAILOVER_SET structure](ns-ntddvol--volume-failover-set.md) | TBD |
| [VOLUME_GET_GPT_ATTRIBUTES_INFORMATION structure](ns-ntddvol--volume-get-gpt-attributes-information.md) | TBD |
| [CSV_CACHE_CALLBACK_V3_OUTPUT structure](ns-ntddvol--csv-cache-callback-v3-output~r1.md) | TBD |
| [VOLUME_ALLOCATION_HINT_OUTPUT structure](ns-ntddvol--volume-allocation-hint-output.md) | TBD |
| [VOLUME_PHYSICAL_OFFSET structure](ns-ntddvol--volume-physical-offset.md) | The VOLUME_PHYSICAL_OFFSET structure contains a physical offset into a volume and its accompanying physical disk number and is used with IOCTL_VOLUME_PHYSICAL_TO_LOGICAL and IOCTL_VOLUME_LOGICAL_TO_PHYSICAL to request a logical offset equivalent of a physical offset or a physical offset equivalent of a logical offset, respectively. |
| [CSV_BLOCKCACHE_CALLBACK structure](ns-ntddvol--csv-blockcache-callback.md) | TBD |
| [CSV_CACHE_CALLBACK_V2_INPUT structure](ns-ntddvol--csv-cache-callback-v2-input.md) | TBD |
| [VOLUME_GET_BC_PROPERTIES_INPUT structure](ns-ntddvol--volume-get-bc-properties-input.md) | TBD |
| [CSV_CACHE_CALLBACK_V2_OUTPUT structure](ns-ntddvol--csv-cache-callback-v2-output~r1.md) | TBD |
| [VOLUME_DISK_EXTENTS structure](ns-ntddvol--volume-disk-extents.md) | The VOLUME_DISK_EXTENTS structure is used in conjunction with the IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS request to retrieve information about all the extents on a given volume. |
| [CSV_FILECACHE_IO_CONTEXT structure](ns-ntddvol--csv-filecache-io-context.md) | TBD |
| [CSV_CACHE_CALLBACK_V3_INPUT structure](ns-ntddvol--csv-cache-callback-v3-input.md) | TBD |
| [CSV_CACHE_CALLBACK_V3_OUTPUT structure](ns-ntddvol--csv-cache-callback-v3-output.md) | TBD |
| [VOLUME_LOGICAL_OFFSET structure](ns-ntddvol--volume-logical-offset.md) | The VOLUME_LOGICAL_OFFSET structure contains a logical offset into a volume. |
| [DISK_EXTENT structure](ns-ntddvol--disk-extent.md) | The DISK_EXTENT structure contains information defining the location and length of a volume extent on a disk. |
| [CSV_FILECACHE_IO_RANGE structure](ns-ntddvol--csv-filecache-io-range.md) | TBD |
| [VOLUME_PHYSICAL_OFFSETS structure](ns-ntddvol--volume-physical-offsets.md) | The VOLUME_PHYSICAL_OFFSETS structure contains an array of physical offsets and accompanying physical disk numbers and is used with IOCTL_VOLUME_LOGICAL_TO_PHYSICAL to request a series of pairs of physical offsets and disk numbers that correspond to a single logical offset. |
| [VOLUME_ALLOCATE_BC_STREAM_OUTPUT structure](ns-ntddvol--volume-allocate-bc-stream-output.md) | TBD |
| [VOLUME_ALLOCATE_BC_STREAM_INPUT structure](ns-ntddvol--volume-allocate-bc-stream-input.md) | TBD |
| [CSV_CACHE_CALLBACK_V2_OUTPUT structure](ns-ntddvol--csv-cache-callback-v2-output.md) | TBD |
| [VOLUME_NUMBER structure](ns-ntddvol--volume-number.md) | TBD |
| [CSV_FILECACHE_FILE_CONTEXT_EXTENSION structure](ns-ntddvol--csv-filecache-file-context-extension.md) | TBD |
| [VOLUME_CRITICAL_IO structure](ns-ntddvol--volume-critical-io.md) | TBD |
| [CSV_FILECACHE_CONTEXT structure](ns-ntddvol--csv-filecache-context.md) | TBD |
| [VOLUME_SHRINK_INFO structure](ns-ntddvol--volume-shrink-info.md) | TBD |
| [FILE_EXTENT structure](ns-ntddvol--file-extent.md) | TBD |
| [VOLUME_READ_PLEX_INPUT structure](ns-ntddvol--volume-read-plex-input.md) | This structure is used in conjunction with IOCTL_VOLUME_READ_PLEX to read data from a specific plex in a volume. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_VOLUME_PREPARE_FOR_SHRINK IOCTL](ni-ntddvol-ioctl-volume-prepare-for-shrink.md) | TBD |
| [IOCTL_VOLUME_IS_CLUSTERED IOCTL](ni-ntddvol-ioctl-volume-is-clustered.md) | TBD |
| [IOCTL_VOLUME_SET_GPT_ATTRIBUTES IOCTL](ni-ntddvol-ioctl-volume-set-gpt-attributes.md) | TBD |
| [IOCTL_VOLUME_BASE IOCTL](ni-ntddvol-ioctl-volume-base.md) | TBD |
| [IOCTL_VOLUME_ALLOCATE_BC_STREAM IOCTL](ni-ntddvol-ioctl-volume-allocate-bc-stream.md) | TBD |
| [IOCTL_VOLUME_PHYSICAL_TO_LOGICAL IOCTL](ni-ntddvol-ioctl-volume-physical-to-logical.md) | TBD |
| [IOCTL_VOLUME_FREE_BC_STREAM IOCTL](ni-ntddvol-ioctl-volume-free-bc-stream.md) | TBD |
| [IOCTL_VOLUME_QUERY_VOLUME_NUMBER IOCTL](ni-ntddvol-ioctl-volume-query-volume-number.md) | TBD |
| [IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE IOCTL](ni-ntddvol-ioctl-volume-supports-online-offline.md) | TBD |
| [IOCTL_VOLUME_OFFLINE IOCTL](ni-ntddvol-ioctl-volume-offline.md) | TBD |
| [IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS IOCTL](ni-ntddvol-ioctl-volume-get-volume-disk-extents.md) | TBD |
| [IOCTL_VOLUME_LOGICAL_TO_PHYSICAL IOCTL](ni-ntddvol-ioctl-volume-logical-to-physical.md) | TBD |
| [IOCTL_VOLUME_READ_PLEX IOCTL](ni-ntddvol-ioctl-volume-read-plex.md) | TBD |
| [IOCTL_VOLUME_UPDATE_PROPERTIES IOCTL](ni-ntddvol-ioctl-volume-update-properties.md) | TBD |
| [IOCTL_VOLUME_IS_DYNAMIC IOCTL](ni-ntddvol-ioctl-volume-is-dynamic.md) | TBD |
| [IOCTL_VOLUME_QUERY_FAILOVER_SET IOCTL](ni-ntddvol-ioctl-volume-query-failover-set.md) | TBD |
| [IOCTL_VOLUME_PREPARE_FOR_CRITICAL_IO IOCTL](ni-ntddvol-ioctl-volume-prepare-for-critical-io.md) | TBD |
| [IOCTL_VOLUME_GET_BC_PROPERTIES IOCTL](ni-ntddvol-ioctl-volume-get-bc-properties.md) | TBD |
| [IOCTL_VOLUME_GET_CSVBLOCKCACHE_CALLBACK IOCTL](ni-ntddvol-ioctl-volume-get-csvblockcache-callback.md) | TBD |
| [IOCTL_VOLUME_GET_GPT_ATTRIBUTES IOCTL](ni-ntddvol-ioctl-volume-get-gpt-attributes.md) | TBD |
| [IOCTL_VOLUME_IS_IO_CAPABLE IOCTL](ni-ntddvol-ioctl-volume-is-io-capable.md) | TBD |
| [IOCTL_VOLUME_QUERY_ALLOCATION_HINT IOCTL](ni-ntddvol-ioctl-volume-query-allocation-hint.md) | TBD |
| [IOCTL_VOLUME_BC_VERSION IOCTL](ni-ntddvol-ioctl-volume-bc-version.md) | TBD |
| [IOCTL_VOLUME_ONLINE IOCTL](ni-ntddvol-ioctl-volume-online.md) | TBD |
| [IOCTL_VOLUME_IS_PARTITION IOCTL](ni-ntddvol-ioctl-volume-is-partition.md) | TBD |
| [IOCTL_VOLUME_QUERY_MINIMUM_SHRINK_SIZE IOCTL](ni-ntddvol-ioctl-volume-query-minimum-shrink-size.md) | TBD |
| [IOCTL_VOLUME_IS_CSV IOCTL](ni-ntddvol-ioctl-volume-is-csv.md) | TBD |
| [IOCTL_VOLUME_IS_OFFLINE IOCTL](ni-ntddvol-ioctl-volume-is-offline.md) | TBD |
| [IOCTL_VOLUME_POST_ONLINE IOCTL](ni-ntddvol-ioctl-volume-post-online.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [CSV_FILECACHE_COMPLETE_CACHE_MISS callback function](nc-ntddvol-csv-filecache-complete-cache-miss.md) | TBD |
| [CSV_BLOCKCACHE_DISABLE_CACHE callback function](nc-ntddvol-csv-blockcache-disable-cache.md) | TBD |
| [CSV_FILECACHE_CLEANUP_CACHE callback function](nc-ntddvol-csv-filecache-cleanup-cache.md) | TBD |
| [CSV_FILECACHE_FILE_CLOSE callback function](nc-ntddvol-csv-filecache-file-close.md) | TBD |
| [CSV_FILECACHE_FILE_SET_EXTENSION callback function](nc-ntddvol-csv-filecache-file-set-extension.md) | TBD |
| [CSV_FILECACHE_PURGE_RDCACHE callback function](nc-ntddvol-csv-filecache-purge-rdcache.md) | TBD |
| [CSV_FILECACHE_HANDLE_CACHE_IO_V2 callback function](nc-ntddvol-csv-filecache-handle-cache-io-v2.md) | TBD |
| [CSV_FILECACHE_HANDLE_CACHE_MISS callback function](nc-ntddvol-csv-filecache-handle-cache-miss.md) | TBD |
| [CSV_FILECACHE_HANDLE_CACHE_IO callback function](nc-ntddvol-csv-filecache-handle-cache-io.md) | TBD |
| [CSV_BLOCKCACHE_PURGE_CACHE callback function](nc-ntddvol-csv-blockcache-purge-cache.md) | TBD |
| [CSV_FILECACHE_HANDLE_CACHE_MISS_V2 callback function](nc-ntddvol-csv-filecache-handle-cache-miss-v2.md) | TBD |
| [CSV_FILECACHE_FILE_GET_EXTENSION callback function](nc-ntddvol-csv-filecache-file-get-extension.md) | TBD |
| [CSV_BLOCKCACHE_ENABLE_CACHE callback function](nc-ntddvol-csv-blockcache-enable-cache.md) | TBD |
| [CSV_FILECACHE_FILE_CREATE callback function](nc-ntddvol-csv-filecache-file-create.md) | TBD |
| [CSV_FILECACHE_COMPLETE_CACHE_MISS_V2 callback function](nc-ntddvol-csv-filecache-complete-cache-miss-v2.md) | TBD |
| [CSV_FILECACHE_COMPLETE_CACHE_IO_V2 callback function](nc-ntddvol-csv-filecache-complete-cache-io-v2.md) | TBD |
| [CSV_FILECACHE_COMPLETE_CACHE_IO callback function](nc-ntddvol-csv-filecache-complete-cache-io.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [CSV_FILECACHE_IO_TYPE enumeration](ne-ntddvol--csv-filecache-io-type.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
