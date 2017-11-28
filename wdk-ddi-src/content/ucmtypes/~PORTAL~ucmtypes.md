# Ucmtypes.h header


This header is used by unknown technology.

Ucmtypes.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCM_PD_POWER_DATA_OBJECT_GET_TYPE function](nf-ucmtypes-ucm-pd-power-data-object-get-type.md) | Retrieves the type of Power Data Object from the UCM_PD_POWER_DATA_OBJECT structure. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_BATTERY function](nf-ucmtypes-ucm-pd-power-data-object-init-battery.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure as a Battery Supply type Power Data Object. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_FIXED function](nf-ucmtypes-ucm-pd-power-data-object-init-fixed.md) | Initializes a to the UCM_PD_POWER_DATA_OBJECT for a Fixed Supply type Power Data Object. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_ULONG function](nf-ucmtypes-ucm-pd-power-data-object-init-ulong.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure by interpreting Power Data Object values and sets each field correctly. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_VARIABLE_NON_BATTERY function](nf-ucmtypes-ucm-pd-power-data-object-init-variable-non-battery.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure as a Variable Supply Non Battery type Power Data Object. |
| [UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG function](nf-ucmtypes-ucm-pd-request-data-object-init-ulong.md) | Initializes a UCM_PD_REQUEST_DATA_OBJECT structure by interpreting Request Data Object values and sets each field correctly. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [UCM_PD_POWER_DATA_OBJECT structure](ns-ucmtypes--ucm-pd-power-data-object.md) | Describes a Power Data Object. For information about these members, see the Power Delivery specification. |
| [UCM_PD_REQUEST_DATA_OBJECT structure](ns-ucmtypes--ucm-pd-request-data-object.md) | Describes a Request Data Object (RDO). For information about these members, see the Power Delivery specification. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [UCM_CHARGING_STATE enumeration](ne-ucmtypes--ucm-charging-state.md) | Defines the charging state of a Type-C connector. |
| [UCM_PD_CONN_STATE enumeration](ne-ucmtypes--ucm-pd-conn-state.md) | Defines power delivery (PD) negotiation states of a Type-C port. |
| [UCM_PD_POWER_DATA_OBJECT_TYPE enumeration](ne-ucmtypes--ucm-pd-power-data-object-type.md) | Defines Power Data Object types. |
| [UCM_POWER_ROLE enumeration](ne-ucmtypes--ucm-power-role.md) | Defines power roles of USB Type-C connected devices. |
| [UCM_TYPEC_CURRENT enumeration](ne-ucmtypes--ucm-typec-current.md) | Defines different Type-C current levels, as defined in the Type-C specification. |
| [UCM_TYPEC_OPERATING_MODE enumeration](ne-ucmtypes--ucm-typec-operating-mode.md) | Defines operating modes of a USB Type-C connector. |
| [UCM_TYPEC_PARTNER enumeration](ne-ucmtypes--ucm-typec-partner.md) | Defines the state of the Type-C connector. |
