---
UID: NS:wwan._WWAN_BASE_STATIONS_INFO
title: "_WWAN_BASE_STATIONS_INFO"
author: windows-driver-content
description: The WWAN_BASE_STATIONS_INFO structure represents information about both serving and neighboring base stations.
old-location: netvista\wwan_base_stations_info.htm
old-project: netvista
ms.assetid: 66460B28-C2B4-4F05-A133-31A753AF9489
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_BASE_STATIONS_INFO, PWWAN_BASE_STATIONS_INFO, PWWAN_BASE_STATIONS_INFO structure pointer [Network Drivers Starting with Windows Vista], WWAN_BASE_STATIONS_INFO, WWAN_BASE_STATIONS_INFO structure [Network Drivers Starting with Windows Vista], _WWAN_BASE_STATIONS_INFO, netvista.wwan_base_stations_info, wwan/PWWAN_BASE_STATIONS_INFO, wwan/WWAN_BASE_STATIONS_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_BASE_STATIONS_INFO
product: Windows
targetos: Windows
req.typenames: WWAN_BASE_STATIONS_INFO, *PWWAN_BASE_STATIONS_INFO
req.product: Windows 10 or later.
---

# _WWAN_BASE_STATIONS_INFO structure
The <b>WWAN_BASE_STATIONS_INFO</b> structure represents information about both serving and neighboring base stations.

## Syntax
````
typedef struct _WWAN_BASE_STATIONS_INFO {
  ULONG SystemType;
  ULONG GSMServingCellOffset;
  ULONG GSMServingCellSize;
  ULONG UMTSServingCellOffset;
  ULONG UMTSServingCellSize;
  ULONG TDSCDMAServingCellOffset;
  ULONG TDSCDMAServingCellSize;
  ULONG LTEServingCellOffset;
  ULONG LTEServingCellSize;
  ULONG GSMNmrOffset;
  ULONG GSMNmrSize;
  ULONG UMTSMrlOffset;
  ULONG UMTSMrlSize;
  ULONG TDSCDMAMrlOffset;
  ULONG TDSCDMAMrlSize;
  ULONG LTEMrlOffset;
  ULONG LTEMrlSize;
  ULONG CDMAMrlOffset;
  ULONG CDMAMrlSize;
  BYTE  BaseStationsData[ANYSIZE_ARRAY];
} WWAN_BASE_STATIONS_INFO, *PWWAN_BASE_STATIONS_INFO;
````

## Members


`SystemType`

Indicates the system type (or types) for which serving cell information is valid. This member is a bitmask of one or more system types as defined in the <b>WwanDataClass</b> member of <a href="..\wwan\ns-wwan-_wwan_device_caps.md">WWAN_DEVICE_CAPS</a>.

`GSMServingCellOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM serving cell information. This member can be NULL when the technology of the serving cell is not GSM.

`GSMServingCellSize`

The size, in bytes, used for the buffer containing the GSM serving cell info, which is formatted as <a href="..\wwan\ns-wwan-_wwan_gsm_serving_cell_info.md">WWAN_GSM_SERVING_CELL_INFO</a>.

`UMTSServingCellOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing the UMTS serving cell information. This member can be NULL when the technology of serving cell is not UMTS.

`UMTSServingCellSize`

The size, in bytes, used for the buffer containing the UMTS serving cell info, which is formatted as <a href="..\wwan\ns-wwan-_wwan_umts_serving_cell_info.md">WWAN_UMTS_SERVING_CELL_INFO</a>.

`TDSCDMAServingCellOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing the TDSCDMA serving cell information. This member can be NULL when the technology of serving cell is not TDSCDMA.

`TDSCDMAServingCellSize`

The size, in bytes, used for the buffer containing the TDSCDMA serving cell info, which is formatted as <a href="..\wwan\ns-wwan-_wwan_tdscdma_serving_cell_info.md">WWAN_TDSCDMA_SERVING_CELL_INFO</a>.

`LTEServingCellOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing the LTE serving cell information. This member can be NULL when the technology of serving cell is not LTE.

`LTEServingCellSize`

The size, in bytes, used for the buffer containing the LTE serving cell info, which is formatted as <a href="..\wwan\ns-wwan-_wwan_lte_serving_cell_info.md">WWAN_LTE_SERVING_CELL_INFO</a>.

`GSMNmrOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM network measurement report. This member can be NULL when no GSM neighboring network is returned in the measurement report.

`GSMNmrSize`

The size, in bytes, of the buffer containing the GSM network measurement report (NMR), which is formatted as <a href="..\wwan\ns-wwan-_wwan_gsm_nmr.md">WWAN_GSM_NMR</a>.

`UMTSMrlOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing UMTS measured results list. This member can be NULL when no UMTS neighboring network is returned in the measurement report.

`UMTSMrlSize`

The size, in bytes, of the buffer containing the UMTS measured results list (MRL), which is formatted as <a href="..\wwan\ns-wwan-_wwan_umts_mrl.md">WWAN_UMTS_MRL</a>.

`TDSCDMAMrlOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing TDSCDMA measured results list. This member can be NULL when no TDSCDMA neighboring network is returned in the measurement report.

`TDSCDMAMrlSize`

The size, in bytes, of the buffer containing the TDSCDMA measured results list (MRL), which is formatted as <a href="..\wwan\ns-wwan-_wwan_tdscdma_mrl.md">WWAN_TDSCDMA_MRL</a>.

`LTEMrlOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing LTE measured results list. This member can be NULL when no LTE neighboring network is returned in the measurement report.

`LTEMrlSize`

The size, in bytes, of the buffer containing the LTE measured results list (MRL), which is formatted as <a href="..\wwan\ns-wwan-_wwan_lte_mrl.md">WWAN_LTE_MRL</a>.

`CDMAMrlOffset`

The offset in bytes, calculated from the beginning of this structure, to the buffer containing CDMA measured results list. This member can be NULL when no CDMA neighboring network is returned in the measurement report.

`CDMAMrlSize`

The size, in bytes, of the buffer containing the CDMA measured results list (MRL), which is formatted as <a href="..\wwan\ns-wwan-_wwan_cdma_mrl.md">WWAN_CDMA_MRL</a>.

`BaseStationsData`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_device_caps.md">WWAN_DEVICE_CAPS</a>



<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_base_stations_info.md">NDIS_WWAN_BASE_STATIONS_INFO</a>



<a href="..\wwan\ns-wwan-_wwan_gsm_nmr.md">WWAN_GSM_NMR</a>



<a href="..\wwan\ns-wwan-_wwan_umts_serving_cell_info.md">WWAN_UMTS_SERVING_CELL_INFO</a>



<a href="..\wwan\ns-wwan-_wwan_gsm_serving_cell_info.md">WWAN_GSM_SERVING_CELL_INFO</a>



<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>



<a href="..\wwan\ns-wwan-_wwan_umts_mrl.md">WWAN_UMTS_MRL</a>



<a href="..\wwan\ns-wwan-_wwan_lte_serving_cell_info.md">WWAN_LTE_SERVING_CELL_INFO</a>



<a href="..\wwan\ns-wwan-_wwan_cdma_mrl.md">WWAN_CDMA_MRL</a>



<a href="..\wwan\ns-wwan-_wwan_tdscdma_mrl.md">WWAN_TDSCDMA_MRL</a>



<a href="..\wwan\ns-wwan-_wwan_lte_mrl.md">WWAN_LTE_MRL</a>



<a href="..\wwan\ns-wwan-_wwan_tdscdma_serving_cell_info.md">WWAN_TDSCDMA_SERVING_CELL_INFO</a>