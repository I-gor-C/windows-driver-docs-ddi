# Declarations in the ehstorbandmgmt header
This header Ehstorbandmgmt contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_EHSTOR_BANDMGMT_ACTIVATE IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-activate.md) | TBD |
| [IOCTL_EHSTOR_TCGDRV_RELINQUISH_SILO IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-tcgdrv-relinquish-silo.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_CREATE_BAND IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-create-band.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-enumerate-bands.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-get-band-metadata.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_REVERT IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-revert.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-set-band-location.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-set-band-metadata.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-query-capabilities.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-set-band-security.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_DELETE_BAND IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-delete-band.md) | TBD |
| [IOCTL_EHSTOR_BANDMGMT_ERASE_BAND IOCTL](ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-erase-band.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [ALGOIDTYPE enumeration](ne-ehstorbandmgmt-algoidtype.md) | TBD |
| [LOCKSTATE enumeration](ne-ehstorbandmgmt-lockstate.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BAND_SECURITY_INFO structure](ns-ehstorbandmgmt--band-security-info.md) | The BAND_SECURITY_INFO structure specifies the security information for a band table entry query. |
| [SET_BAND_METADATA_PARAMETERS structure](ns-ehstorbandmgmt--set-band-metadata-parameters.md) | The metadata for a configured band is set to the parameters in a SET_BAND_METADATA_PARAMETERS structure. This structure is input for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA request. |
| [DELETE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--delete-band-parameters.md) | A configured band is deleted according to the parameters in a DELETE_BAND_PARAMETERS structure. This structure is input for an IOCTL_EHSTOR_BANDMGMT_DELETE_BAND request. |
| [ERASE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--erase-band-parameters.md) | The ERASE_BAND_PARAMETERS structure contains the selection criteria for a band to erase. Additionally, a new authentication key can be set. This structure is input for an IOCTL_EHSTOR_BANDMGMT_ERASE_BAND request. |
| [BAND_MANAGEMENT_CAPABILITIES structure](ns-ehstorbandmgmt--band-management-capabilities.md) | The BAND_MANAGEMENT_CAPABILITIES structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES request. |
| [SET_BAND_SECURITY_PARAMETERS structure](ns-ehstorbandmgmt--set-band-security-parameters.md) | The parameters to set security properties for a band on a storage device for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY request are specified in a SET_BAND_SECURITY_PARAMETERS structure. |
| [CREATE_BAND_PARAMETERS structure](ns-ehstorbandmgmt--create-band-parameters.md) | The parameters to create a band on a storage device for an IOCTL_EHSTOR_BANDMGMT_CREATE_BAND request are specified in a CREATE_BAND_PARAMETERS structure. |
| [AUTH_KEY structure](ns-ehstorbandmgmt--auth-key.md) | TBD |
| [SET_BAND_LOCATION_PARAMETERS structure](ns-ehstorbandmgmt--set-band-location-parameters.md) | The SET_BAND_LOCATION_PARAMETERS structure specifies the parameters to set location properties for a band on a storage device for a IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION request. |
| [ENUMERATE_BANDS_PARAMETERS structure](ns-ehstorbandmgmt--enumerate-bands-parameters.md) | The ENUMERATE_BANDS_PARAMETERS structure is used to select which band information entries are selected for return from an IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS request. |
| [GET_BAND_METADATA_PARAMETERS structure](ns-ehstorbandmgmt--get-band-metadata-parameters.md) | The metadata for a configured band is retrieved according to the parameters in a GET_BAND_METADATA_PARAMETERS structure. This structure is input for an IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA request. |
| [BAND_TABLE_ENTRY structure](ns-ehstorbandmgmt--band-table-entry.md) | Banding information entries in BAND_TABLE are represented as BAND_TABLE_ENTRY structures. These entries contain location and security properties for a band configuration. |
| [ACTIVATE_REVERT_PARAMETERS structure](ns-ehstorbandmgmt--activate-revert-parameters.md) | TBD |
| [BAND_TABLE structure](ns-ehstorbandmgmt--band-table.md) | The BAND_TABLE structure contains the table of bands returned from an IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS request. |
| [BAND_LOCATION_INFO structure](ns-ehstorbandmgmt--band-location-info.md) | The BAND_LOCATION_INFO structure specifies the location information for a band table entry query. |

This header is used in these topics:

- [Storage](..content/_Storage)
