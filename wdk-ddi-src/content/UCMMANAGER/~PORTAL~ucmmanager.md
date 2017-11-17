# Declarations in the ucmmanager header
This header Ucmmanager contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_CONNECTOR_TYPEC_CONFIG_INIT function](nf-ucmmanager-ucm-connector-typec-config-init.md) | Initializes the UCM_CONNECTOR_TYPEC_CONFIG structure. |
| [UcmConnectorPdPartnerSourceCaps function](nf-ucmmanager-ucmconnectorpdpartnersourcecaps.md) | TBD |
| [UcmConnectorChargingStateChanged function](nf-ucmmanager-ucmconnectorchargingstatechanged.md) | TBD |
| [UcmConnectorTypeCAttach function](nf-ucmmanager-ucmconnectortypecattach.md) | TBD |
| [UcmConnectorPdConnectionStateChanged function](nf-ucmmanager-ucmconnectorpdconnectionstatechanged.md) | TBD |
| [UCM_CONNECTOR_CONFIG_INIT function](nf-ucmmanager-ucm-connector-config-init.md) | Initializes a UCM_CONNECTOR_CONFIG structure. |
| [UcmConnectorTypeCDetach function](nf-ucmmanager-ucmconnectortypecdetach.md) | TBD |
| [UCM_CONNECTOR_PD_CONFIG_INIT function](nf-ucmmanager-ucm-connector-pd-config-init.md) | Initializes a UCM_CONNECTOR_PD_CONFIG structure. |
| [UCM_MANAGER_CONFIG_INIT function](nf-ucmmanager-ucm-manager-config-init.md) | Initializes a UCM_MANAGER_CONFIG structure. |
| [UcmConnectorCreate function](nf-ucmmanager-ucmconnectorcreate.md) | TBD |
| [UcmInitializeDevice function](nf-ucmmanager-ucminitializedevice.md) | TBD |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS_INIT function](nf-ucmmanager-ucm-connector-pd-conn-state-changed-params-init.md) | Initializes a UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure. |
| [UcmConnectorPdSourceCaps function](nf-ucmmanager-ucmconnectorpdsourcecaps.md) | TBD |
| [UcmConnectorPowerDirectionChanged function](nf-ucmmanager-ucmconnectorpowerdirectionchanged.md) | TBD |
| [UcmConnectorTypeCCurrentAdChanged function](nf-ucmmanager-ucmconnectortypeccurrentadchanged.md) | TBD |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS_INIT function](nf-ucmmanager-ucm-connector-typec-attach-params-init.md) | Initializes a UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure. |
| [UcmConnectorDataDirectionChanged function](nf-ucmmanager-ucmconnectordatadirectionchanged.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_UCMCONNECTORPOWERDIRECTIONCHANGED callback function](nc-ucmmanager-pfn-ucmconnectorpowerdirectionchanged.md) | TBD |
| [PFN_UCMCONNECTORCREATE callback function](nc-ucmmanager-pfn-ucmconnectorcreate.md) | TBD |
| [PFN_UCMCONNECTORTYPECDETACH callback function](nc-ucmmanager-pfn-ucmconnectortypecdetach.md) | TBD |
| [PFN_UCMCONNECTORTYPECCURRENTADCHANGED callback function](nc-ucmmanager-pfn-ucmconnectortypeccurrentadchanged.md) | TBD |
| [PFN_UCMCONNECTORCHARGINGSTATECHANGED callback function](nc-ucmmanager-pfn-ucmconnectorchargingstatechanged.md) | TBD |
| [EVT_UCM_CONNECTOR_SET_DATA_ROLE callback](nc-ucmmanager-evt-ucm-connector-set-data-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_DATA_ROLE event callback function that swaps the data role of the connector to the specified role when attached to a partner connector. |
| [PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED callback function](nc-ucmmanager-pfn-ucmconnectorpdconnectionstatechanged.md) | TBD |
| [PFN_UCMCONNECTORPDPARTNERSOURCECAPS callback function](nc-ucmmanager-pfn-ucmconnectorpdpartnersourcecaps.md) | TBD |
| [EVT_UCM_CONNECTOR_SET_POWER_ROLE callback](nc-ucmmanager-evt-ucm-connector-set-power-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_POWER_ROLE event callback function that sets the power role of the connector to the specified role when attached to a partner connector. |
| [PFN_UCMCONNECTORPDSOURCECAPS callback function](nc-ucmmanager-pfn-ucmconnectorpdsourcecaps.md) | TBD |
| [PFN_UCMINITIALIZEDEVICE callback function](nc-ucmmanager-pfn-ucminitializedevice.md) | TBD |
| [PFN_UCMCONNECTORDATADIRECTIONCHANGED callback function](nc-ucmmanager-pfn-ucmconnectordatadirectionchanged.md) | TBD |
| [PFN_UCMCONNECTORTYPECATTACH callback function](nc-ucmmanager-pfn-ucmconnectortypecattach.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_CONNECTOR_PD_CONFIG structure](ns-ucmmanager--ucm-connector-pd-config.md) | Describes the Power Delivery 2.0 capabilities of the connector. |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure](ns-ucmmanager--ucm-connector-typec-attach-params.md) | Describes the partner that is currently attached to the connector. |
| [UCM_MANAGER_CONFIG structure](ns-ucmmanager--ucm-manager-config.md) | Describes the configuration options for the UCM Manager. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure](ns-ucmmanager--ucm-connector-pd-conn-state-changed-params.md) | Describes the parameters for PD connection changed event. |
| [UCM_CONNECTOR_CONFIG structure](ns-ucmmanager--ucm-connector-config.md) | Describes the configuration options for a Type-C connector object. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
| [UCM_CONNECTOR_TYPEC_CONFIG structure](ns-ucmmanager--ucm-connector-typec-config.md) | Describes the configuration options for a Type-C connector. |

This header is used in these topics:

- [usbref](..content/_usbref)
