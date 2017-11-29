# Ehstorbandmgmt.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ehstorbandmgmt.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [BAND_LOCATION_INFO structure](ns-ehstorbandmgmt--band-location-info.md) | The BAND_LOCATION_INFO structure specifies the location information for a band table entry query. |
| [BAND_MANAGEMENT_CAPABILITIES structure](ns-ehstorbandmgmt--band-management-capabilities.md) | The BAND_MANAGEMENT_CAPABILITIES structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES request. |
| [BAND_SECURITY_INFO structure](ns-ehstorbandmgmt--band-security-info.md) | The BAND_SECURITY_INFO structure specifies the security information for a band table entry query. |
| [BAND_TABLE structure](ns-ehstorbandmgmt--band-table.md) | The BAND_TABLE structure contains the table of bands returned from an IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS request. |
| [BAND_TABLE_ENTRY structure](ns-ehstorbandmgmt--band-table-entry.md) | Banding information entries in BAND_TABLE are represented as BAND_TABLE_ENTRY structures. These entries contain location and security properties for a band configuration. |
| [CREATE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--create-band-parameters.md) | The parameters to create a band on a storage device for an IOCTL_EHSTOR_BANDMGMT_CREATE_BAND request are specified in a CREATE_BAND_PARAMETERS structure. |
| [DELETE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--delete-band-parameters.md) | A configured band is deleted according to the parameters in a DELETE_BAND_PARAMETERS structure. This structure is input for an IOCTL_EHSTOR_BANDMGMT_DELETE_BAND request. |
| [ENUMERATE_BANDS_PARAMETERS structure](ns-ehstorbandmgmt--enumerate-bands-parameters.md) | The ENUMERATE_BANDS_PARAMETERS structure is used to select which band information entries are selected for return from an IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS request. |
| [ERASE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--erase-band-parameters.md) | The ERASE_BAND_PARAMETERS structure contains the selection criteria for a band to erase. Additionally, a new authentication key can be set. This structure is input for an IOCTL_EHSTOR_BANDMGMT_ERASE_BAND request. |
| [GET_BAND_METADATA_PARAMETERS structure](ns-ehstorbandmgmt--get-band-metadata-parameters.md) | The metadata for a configured band is retrieved according to the parameters in a GET_BAND_METADATA_PARAMETERS structure. This structure is input for an IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA request. |
| [SET_BAND_LOCATION_PARAMETERS structure](ns-ehstorbandmgmt--set-band-location-parameters.md) | The SET_BAND_LOCATION_PARAMETERS structure specifies the parameters to set location properties for a band on a storage device for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION request. |
| [SET_BAND_METADATA_PARAMETERS structure](ns-ehstorbandmgmt--set-band-metadata-parameters.md) | The metadata for a configured band is set to the parameters in a SET_BAND_METADATA_PARAMETERS structure. This structure is input for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA request. |
| [SET_BAND_SECURITY_PARAMETERS structure](ns-ehstorbandmgmt--set-band-security-parameters.md) | The parameters to set security properties for a band on a storage device for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY request are specified in a SET_BAND_SECURITY_PARAMETERS structure. |
