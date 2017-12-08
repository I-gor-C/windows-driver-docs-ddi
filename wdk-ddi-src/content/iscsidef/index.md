# Iscsidef.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Iscsidef.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ISCSI_IP_Address structure](ns-iscsidef--iscsi-ip-address.md) | The ISCSI_IP_Address structure defines an IP address. |
| [ISCSI_LUNList structure](ns-iscsidef--iscsi-lunlist.md) | The ISCSI_LUNList structure defines a mapping between the LUN number that is used by the operating system and the LUN number that is configured in the iSCSI target. |
| [ISCSI_LoginOptions structure](ns-iscsidef--iscsi-loginoptions.md) | The ISCSI_LoginOptions structure defines the characteristics of a logon session. The LoginToTarget_IN routines use these defined characteristics while it logs into an iSCSI target. |
| [ISCSI_TargetMapping structure](ns-iscsidef--iscsi-targetmapping.md) | The ISCSI_TargetMapping structure maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI logical unit numbers. |
| [ISCSI_TargetPortal structure](ns-iscsidef--iscsi-targetportal.md) | The ISCSI_TargetPortal structure provides a definition of a target portal. |
| [ISCSI_TargetPortalGroup structure](ns-iscsidef--iscsi-targetportalgroup.md) | The ISCSI_TargetPortalGroup structure provides a definition of a target portal group. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PISCSIIPADDRESSTYPE enumeration](ne-iscsidef-piscsiipaddresstype.md) | The ISCSIIPADDRESSTYPE enumeration indicates formats for an IP address. |
| [PISCSI_AUTH_TYPES enumeration](ne-iscsidef-piscsi-auth-types.md) | The ISCSI_AUTH_TYPES enumeration indicates the type of authentication method that is used to establish a logon connection. |
| [PISCSI_DIGEST_TYPES enumeration](ne-iscsidef-piscsi-digest-types.md) | The ISCSI_DIGEST_TYPES enumeration indicates the digest type. |
