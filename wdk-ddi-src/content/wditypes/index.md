# Wditypes.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Wditypes.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [WDI_CHANNEL_MAPPING_ENTRY structure](ns-wditypes--wdi-channel-mapping-entry.md) | The WDI_CHANNEL_MAPPING_ENTRY structure defines a channel mapping entry. |
| [WDI_DATA_RATE_ENTRY structure](ns-wditypes--wdi-data-rate-entry.md) | The WDI_DATA_RATE_ENTRY structure defines a data rate entry. |
| [WDI_ETHERTYPE_ENCAPSULATION_ENTRY structure](ns-wditypes--wdi-ethertype-encapsulation-entry.md) | The WDI_ETHERTYPE_ENCAPSULATION_ENTRY structure defines an EtherType encapsulation entry. |
| [WDI_TYPE_MIC structure](ns-wditypes--wdi-type-mic.md) | The WDI_TYPE_MIC structure defines the MIC (802.11r). |
| [WDI_TYPE_NONCE structure](ns-wditypes--wdi-type-nonce.md) | The WDI_TYPE_NONCE structure defines the SNonce or ANonce (802.11r). |
| [WDI_TYPE_PMK_NAME structure](ns-wditypes--wdi-type-pmk-name.md) | The WDI_TYPE_PMK_NAME structure defines the PMKR0Name or PMKR1Name (802.11r). |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDI_ACTION_FRAME_CATEGORY enumeration](ne-wditypes--wdi-action-frame-category.md) | The WDI_ACTION_FRAME_CATEGORY enumeration defines the action frame categories. |
| [WDI_ANQP_QUERY_STATUS enumeration](ne-wditypes--wdi-anqp-query-status.md) | The WDI_ANQP_QUERY_STATUS enumeration defines the Access Network Query Protocol (ANQP) query status values. |
| [WDI_ASSOC_STATUS enumeration](ne-wditypes--wdi-assoc-status.md) | The WDI_ASSOC_STATUS enumeration defines the association status values. |
| [WDI_AUTH_ALGORITHM enumeration](ne-wditypes--wdi-auth-algorithm.md) | The WDI_AUTH_ALGORITHM enumeration defines the authentication algorithm values. |
| [WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration](ne-wditypes--wdi-bluetooth-coexistence-support.md) | The WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration defines Bluetooth coexistence support values. |
| [WDI_BSS_SELECTION_FLAGS enumeration](ne-wditypes--wdi-bss-selection-flags.md) | The WDI_BSS_SELECTION_FLAGS enumeration defines flags for BSS selection. |
| [WDI_CAN_SUSTAIN_AP_REASON enumeration](ne-wditypes--wdi-can-sustain-ap-reason.md) | The WDI_CAN_SUSTAIN_AP_REASON enumeration defines the reasons the port is ready to receive a OID_WDI_TASK_START_AP request. |
| [WDI_CIPHER_ALGORITHM enumeration](ne-wditypes--wdi-cipher-algorithm.md) | The WDI_CIPHER_ALGORITHM enumeration defines the cipher algorithm values. |
| [WDI_CIPHER_KEY_DIRECTION enumeration](ne-wditypes--wdi-cipher-key-direction.md) | The WDI_CIPHER_KEY_DIRECTION enumeration defines the traffic directions decrypted by a cipher key. |
| [WDI_CIPHER_KEY_TYPE enumeration](ne-wditypes--wdi-cipher-key-type.md) | The WDI_CIPHER_KEY_TYPE enumeration defines the cipher key types. |
| [WDI_CONNECTION_QUALITY_HINT enumeration](ne-wditypes--wdi-connection-quality-hint.md) | The WDI_CONNECTION_QUALITY_HINT enumeration defines the Wi-Fi connection quality hints. |
| [WDI_DATA_RATE_FLAGS enumeration](ne-wditypes--wdi-data-rate-flags.md) | The WDI_DATA_RATE_FLAGS enumeration defines the data rate flags. |
| [WDI_DS_INFO enumeration](ne-wditypes--wdi-ds-info.md) | The WDI_DS_INFO enumeration defines values that specify whether the port is connected to the same DS that it was previously associated to. |
| [WDI_ENCAPSULATION_TYPE enumeration](ne-wditypes--wdi-encapsulation-type.md) | The WDI_ENCAPSULATION_TYPE enumeration defines the Wi-Fi encapsulation types. |
| [WDI_EXEMPTION_PACKET_TYPE enumeration](ne-wditypes--wdi-exemption-packet-type.md) | The WDI_EXEMPTION_PACKET_TYPE enumeration defines the types of packet exemptions. |
| [WDI_FIPS_MODE enumeration](ne-wditypes--wdi-fips-mode.md) | The WDI_FIPS_MODE enumeration defines values that specify if FIPS mode is enabled or not. |
| [WDI_IHV_TASK_PRIORITY enumeration](ne-wditypes--wdi-ihv-task-priority.md) | The WDI_IHV_TASK_PRIORITY enumeration defines IHV task priorities. |
| [WDI_P2P_ACTION_FRAME_TYPE enumeration](ne-wditypes--wdi-p2p-action-frame-type.md) | The WDI_P2P_ACTION_FRAME_TYPE enumeration defines the Wi-Fi Direct action frame types. |
| [WDI_P2P_CHANNEL_INDICATE_REASON enumeration](ne-wditypes--wdi-p2p-channel-indicate-reason.md) | The WDI_P2P_CHANNEL_INDICATE_REASON enumeration defines Wi-Fi Direct channel indication reason values. |
| [WDI_P2P_DISCOVER_TYPE enumeration](ne-wditypes--wdi-p2p-discover-type.md) | The WDI_P2P_DISCOVER_TYPE enumeration defines the Wi-Fi Direct discovery types. |
| [WDI_P2P_GO_INTERNAL_RESET_POLICY enumeration](ne-wditypes--wdi-p2p-go-internal-reset-policy.md) | The WDI_P2P_GO_INTERNAL_RESET_POLICY enumeration defines the Wi-Fi Direct Group Owner internal reset policies. |
| [WDI_P2P_LISTEN_STATE enumeration](ne-wditypes--wdi-p2p-listen-state.md) | The WDI_P2P_LISTEN_STATE enumeration defines the Wi-Fi Direct listen states. |
| [WDI_P2P_SCAN_TYPE enumeration](ne-wditypes--wdi-p2p-scan-type.md) | The WDI_P2P_SCAN_TYPE enumeration defines the Wi-Fi Direct scan types. |
| [WDI_P2P_SERVICE_DISCOVERY_TYPE enumeration](ne-wditypes--wdi-p2p-service-discovery-type.md) | The WDI_P2P_SERVICE_DISCOVERY_TYPE enumeration defines the types of service discovery. |
| [WDI_PACKET_FILTER_TYPE enumeration](ne-wditypes--wdi-packet-filter-type.md) | The WDI_PACKET_FILTER_TYPE enumeration defines the packet filter types. |
| [WDI_PHY_TYPE enumeration](ne-wditypes--wdi-phy-type.md) | The WDI_PHY_TYPE enumeration defines the PHY types. |
| [WDI_POWER_MODE_REASON_CODE enumeration](ne-wditypes--wdi-power-mode-reason-code.md) | The WDI_POWER_MODE_REASON_CODE enumeration defines the reasons for entering the Power Save state. |
| [WDI_POWER_SAVE_LEVEL enumeration](ne-wditypes--wdi-power-save-level.md) | The WDI_POWER_SAVE_LEVEL enumeration defines the power save levels. |
| [WDI_QOS_PROTOCOL enumeration](ne-wditypes--wdi-qos-protocol.md) | The WDI_QOS_PROTOCOL enumeration defines Wi-Fi QOS protocols. |
| [WDI_RADIO_MEASUREMENT_ACTION enumeration](ne-wditypes--wdi-radio-measurement-action.md) | The WDI_RADIO_MEASUREMENT_ACTION enumeration defines the radio measurement actions. |
| [WDI_ROAM_TRIGGER enumeration](ne-wditypes--wdi-roam-trigger.md) | The WDI_ROAM_TRIGGER enumeration defines roam triggers. |
| [WDI_SCAN_TRIGGER enumeration](ne-wditypes--wdi-scan-trigger.md) | The WDI_SCAN_TRIGGER enumeration defines the scan trigger values. |
| [WDI_SCAN_TYPE enumeration](ne-wditypes--wdi-scan-type.md) | The WDI_SCAN_TYPE enumeration defines the scan types. |
| [WDI_STOP_AP_REASON enumeration](ne-wditypes--wdi-stop-ap-reason.md) | The WDI_STOP_AP_REASON enumeration defines the reasons an adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs. |
| [WDI_WNM_ACTION enumeration](ne-wditypes--wdi-wnm-action.md) | The WDI_WNM_ACTION enumeration defines the message type for 802.11v BSS Transition Management action frames. |
| [WDI_WPS_CONFIGURATION_METHOD enumeration](ne-wditypes--wdi-wps-configuration-method.md) | The WDI_WPS_CONFIGURATION_METHOD enumeration defines WPS configuration methods. |
