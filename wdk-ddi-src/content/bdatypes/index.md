# Bdatypes.h header


This header is used by Streaming media devices. For more information, see
- [Streaming media devices](../_stream/index.md)

Bdatypes.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [BDANODE_DESCRIPTOR structure](ns-bdatypes--bdanode-descriptor.md) | The BDANODE_DESCRIPTOR structure describes a BDA node. |
| [BDA_BUFFER structure](ns-bdatypes--bda-buffer.md) | . |
| [BDA_CAS_CHECK_ENTITLEMENTTOKEN structure](ns-bdatypes--bda-cas-check-entitlementtoken.md) | . |
| [BDA_CAS_CLOSEMMIDATA structure](ns-bdatypes--bda-cas-closemmidata.md) | . |
| [BDA_CAS_CLOSE_MMIDIALOG structure](ns-bdatypes--bda-cas-close-mmidialog.md) | . |
| [BDA_CAS_OPENMMIDATA structure](ns-bdatypes--bda-cas-openmmidata.md) | . |
| [BDA_CAS_REQUESTTUNERDATA structure](ns-bdatypes--bda-cas-requesttunerdata.md) | . |
| [BDA_CA_MODULE_UI structure](ns-bdatypes--bda-ca-module-ui.md) | The BDA_CA_MODULE_UI structure describes the user interface (UI) that conditional access (CA) plugins can display. |
| [BDA_DISEQC_RESPONSE structure](ns-bdatypes--bda-diseqc-response.md) | . |
| [BDA_DISEQC_SEND structure](ns-bdatypes--bda-diseqc-send.md) | . |
| [BDA_DRM_DRMSTATUS structure](ns-bdatypes--bda-drm-drmstatus.md) | . |
| [BDA_DVBT2_L1_SIGNALLING_DATA structure](ns-bdatypes--bda-dvbt2-l1-signalling-data.md) | . |
| [BDA_ETHERNET_ADDRESS structure](ns-bdatypes--bda-ethernet-address.md) | . |
| [BDA_ETHERNET_ADDRESS_LIST structure](ns-bdatypes--bda-ethernet-address-list.md) | . |
| [BDA_GDDS_DATA structure](ns-bdatypes--bda-gdds-data.md) | . |
| [BDA_GDDS_DATATYPE structure](ns-bdatypes--bda-gdds-datatype.md) | . |
| [BDA_IPv4_ADDRESS structure](ns-bdatypes--bda-ipv4-address.md) | . |
| [BDA_IPv4_ADDRESS_LIST structure](ns-bdatypes--bda-ipv4-address-list.md) | . |
| [BDA_IPv6_ADDRESS structure](ns-bdatypes--bda-ipv6-address.md) | . |
| [BDA_IPv6_ADDRESS_LIST structure](ns-bdatypes--bda-ipv6-address-list.md) | . |
| [BDA_ISDBCAS_REQUESTHEADER structure](ns-bdatypes--bda-isdbcas-requestheader.md) | . |
| [BDA_ISDBCAS_RESPONSEDATA structure](ns-bdatypes--bda-isdbcas-responsedata.md) | . |
| [BDA_PID_MAP structure](ns-bdatypes--bda-pid-map.md) | The BDA_PID_MAP structure describes a type of data to filter out of the input stream of a packet identifier (PID) filter and then pass to a downstream filter. |
| [BDA_PID_UNMAP structure](ns-bdatypes--bda-pid-unmap.md) | The BDA_PID_UNMAP structure describes packet types to stop filtering from the input stream of a packet identifier (PID) filter. These packet types are identified with PIDs. |
| [BDA_PROGRAM_PID_LIST structure](ns-bdatypes--bda-program-pid-list.md) | The BDA_PROGRAM_PID_LIST structure describes data of a specific program to view. This data consists of packets that are identified with packet identifiers (PID). |
| [BDA_RATING_PINRESET structure](ns-bdatypes--bda-rating-pinreset.md) | . |
| [BDA_SCAN_CAPABILTIES structure](ns-bdatypes--bda-scan-capabilties.md) | . |
| [BDA_SCAN_START structure](ns-bdatypes--bda-scan-start.md) | . |
| [BDA_SCAN_STATE structure](ns-bdatypes--bda-scan-state.md) | . |
| [BDA_SIGNAL_TIMEOUTS structure](ns-bdatypes--bda-signal-timeouts.md) | . |
| [BDA_STRING structure](ns-bdatypes--bda-string.md) | . |
| [BDA_TABLE_SECTION structure](ns-bdatypes--bda-table-section.md) | The BDA_TABLE_SECTION structure describes a table section. |
| [BDA_TEMPLATE_CONNECTION structure](ns-bdatypes--bda-template-connection.md) | The BDA_TEMPLATE_CONNECTION structure describes the template for a BDA connection in terms of where it begins and ends. |
| [BDA_TEMPLATE_PIN_JOINT structure](ns-bdatypes--bda-template-pin-joint.md) | The BDA_TEMPLATE_PIN_JOINT structure describes a joint in a template topology. |
| [BDA_TS_SELECTORINFO structure](ns-bdatypes--bda-ts-selectorinfo.md) | . |
| [BDA_TS_SELECTORINFO_ISDBS_EXT structure](ns-bdatypes--bda-ts-selectorinfo-isdbs-ext.md) | . |
| [BDA_TUNER_DIAGNOSTICS structure](ns-bdatypes--bda-tuner-diagnostics.md) | . |
| [BDA_TUNER_TUNERSTATE structure](ns-bdatypes--bda-tuner-tunerstate.md) | . |
| [BDA_USERACTIVITY_INTERVAL structure](ns-bdatypes--bda-useractivity-interval.md) | . |
| [BDA_WMDRMTUNER_PIDPROTECTION structure](ns-bdatypes--bda-wmdrmtuner-pidprotection.md) | . |
| [BDA_WMDRMTUNER_PURCHASEENTITLEMENT structure](ns-bdatypes--bda-wmdrmtuner-purchaseentitlement.md) | . |
| [BDA_WMDRM_KEYINFOLIST structure](ns-bdatypes--bda-wmdrm-keyinfolist.md) | . |
| [BDA_WMDRM_RENEWLICENSE structure](ns-bdatypes--bda-wmdrm-renewlicense.md) | . |
| [BDA_WMDRM_STATUS structure](ns-bdatypes--bda-wmdrm-status.md) | . |
| [MPEG2_TRANSPORT_STRIDE structure](ns-bdatypes--mpeg2-transport-stride.md) | The MPEG2_TRANSPORT_STRIDE structure describes the format block of the MPEG2 transport stride. |
| [PID_MAP structure](ns-bdatypes-pid-map.md) | The PID_MAP structure describes a group of packets in the output stream of a packet identifier (PID) filter. This group consists of packets that are identified with an identical PID and contain particular media content. |
| [tagKS_BDA_FRAME_INFO structure](ns-bdatypes-tagks-bda-frame-info.md) | The KS_BDA_FRAME_INFO structure describes BDA extensions to the KSSTREAM_HEADER structure, which describes a packet of data to be read from or written to a streaming driver pin. |
