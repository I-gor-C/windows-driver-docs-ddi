---
UID: NS.wwan._WWAN_BASE_STATIONS_INFO
title: WWAN_BASE_STATIONS_INFO
author: windows-driver-content
description: The WWAN_BASE_STATIONS_INFO structure represents information about both serving and neighboring base stations.
old-location: netvista\wwan_base_stations_info.htm
ms.assetid: 66460B28-C2B4-4F05-A133-31A753AF9489
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_BASE_STATIONS_INFO
req.alt-loc: wwan.h
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
ms.keywords: WWAN_BASE_STATIONS_INFO, WWAN_BASE_STATIONS_INFO, *PWWAN_BASE_STATIONS_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_BASE_STATIONS_INFO structure



## -description
<p>The <b>WWAN_BASE_STATIONS_INFO</b> structure represents information about both serving and neighboring base stations.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>SystemType</b>

<dd>
<p>Indicates the system type (or types) for which serving cell information is valid. This member is a bitmask of one or more system types as defined in the <b>WwanDataClass</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>.</p>
</dd>

### -field <b>GSMServingCellOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM serving cell information. This member can be NULL when the technology of the serving cell is not GSM.</p>
</dd>

### -field <b>GSMServingCellSize</b>

<dd>
<p>The size, in bytes, used for the buffer containing the GSM serving cell info, which is formatted as <a href="https://msdn.microsoft.com/37F6BD26-55F3-4E46-9C39-97A95B6FF5B1">WWAN_GSM_SERVING_CELL_INFO</a>.</p>
</dd>

### -field <b>UMTSServingCellOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing the UMTS serving cell information. This member can be NULL when the technology of serving cell is not UMTS.</p>
</dd>

### -field <b>UMTSServingCellSize</b>

<dd>
<p>The size, in bytes, used for the buffer containing the UMTS serving cell info, which is formatted as <a href="https://msdn.microsoft.com/62257D65-DCB9-43C3-A862-DAB31C27EF0A">WWAN_UMTS_SERVING_CELL_INFO</a>.</p>
</dd>

### -field <b>TDSCDMAServingCellOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing the TDSCDMA serving cell information. This member can be NULL when the technology of serving cell is not TDSCDMA.</p>
</dd>

### -field <b>TDSCDMAServingCellSize</b>

<dd>
<p>The size, in bytes, used for the buffer containing the TDSCDMA serving cell info, which is formatted as <a href="https://msdn.microsoft.com/5D0DD219-8D81-4F72-B327-119A45CC35B4">WWAN_TDSCDMA_SERVING_CELL_INFO</a>.</p>
</dd>

### -field <b>LTEServingCellOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing the LTE serving cell information. This member can be NULL when the technology of serving cell is not LTE.</p>
</dd>

### -field <b>LTEServingCellSize</b>

<dd>
<p>The size, in bytes, used for the buffer containing the LTE serving cell info, which is formatted as <a href="https://msdn.microsoft.com/17A78DC7-A89D-405A-983E-FC0DC469A4B0">WWAN_LTE_SERVING_CELL_INFO</a>.</p>
</dd>

### -field <b>GSMNmrOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM network measurement report. This member can be NULL when no GSM neighboring network is returned in the measurement report.</p>
</dd>

### -field <b>GSMNmrSize</b>

<dd>
<p>The size, in bytes, of the buffer containing the GSM network measurement report (NMR), which is formatted as <a href="https://msdn.microsoft.com/ADEEB57F-79FF-4AA7-84AF-FED413E47057">WWAN_GSM_NMR</a>.</p>
</dd>

### -field <b>UMTSMrlOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing UMTS measured results list. This member can be NULL when no UMTS neighboring network is returned in the measurement report.</p>
</dd>

### -field <b>UMTSMrlSize</b>

<dd>
<p>The size, in bytes, of the buffer containing the UMTS measured results list (MRL), which is formatted as <a href="https://msdn.microsoft.com/B62F63EB-747A-4672-9A79-5065A8BC04D1">WWAN_UMTS_MRL</a>.</p>
</dd>

### -field <b>TDSCDMAMrlOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing TDSCDMA measured results list. This member can be NULL when no TDSCDMA neighboring network is returned in the measurement report.</p>
</dd>

### -field <b>TDSCDMAMrlSize</b>

<dd>
<p>The size, in bytes, of the buffer containing the TDSCDMA measured results list (MRL), which is formatted as <a href="https://msdn.microsoft.com/D919EF5E-502C-4983-AFC5-F3F6E6CC8C3B">WWAN_TDSCDMA_MRL</a>.</p>
</dd>

### -field <b>LTEMrlOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing LTE measured results list. This member can be NULL when no LTE neighboring network is returned in the measurement report.</p>
</dd>

### -field <b>LTEMrlSize</b>

<dd>
<p>The size, in bytes, of the buffer containing the LTE measured results list (MRL), which is formatted as <a href="https://msdn.microsoft.com/5959B7A7-147D-4F20-82CC-EC1DEAAE3494">WWAN_LTE_MRL</a>.</p>
</dd>

### -field <b>CDMAMrlOffset</b>

<dd>
<p>The offset in bytes, calculated from the beginning of this structure, to the buffer containing CDMA measured results list. This member can be NULL when no CDMA neighboring network is returned in the measurement report.</p>
</dd>

### -field <b>CDMAMrlSize</b>

<dd>
<p>The size, in bytes, of the buffer containing the CDMA measured results list (MRL), which is formatted as <a href="https://msdn.microsoft.com/A19B98B5-F2E5-4AF9-9D2B-A7DD47441656">WWAN_CDMA_MRL</a>.</p>
</dd>

### -field <b>BaseStationsData[ANYSIZE_ARRAY]</b>

<dd>
<p>The data buffer containing the base stations information. This buffer is where the structures specified by the other members of <b>WWAN_BASE_STATIONS_INFO</b> reside: <b>WWAN_GSM_SERVING_CELL_INFO</b>, <b>WWAN_UMTS_SERVING_CELL_INFO</b>, <b>WWAN_TDSCDMA_SERVING_CELL_INFO</b>, <b>WWAN_LTE_SERVING_CELL_INFO</b>, <b>WWAN_GSM_NMR</b>, <b>WWAN_UMTS_MRL</b>, <b>WWAN_TDSCDMA_MRL</b>, <b>WWAN_LTE_MRL</b>, and <b>WWAN_CDMA_MRL</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/7C0E0903-F564-4F2B-95F9-FA8512FEF61B">NDIS_WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/37F6BD26-55F3-4E46-9C39-97A95B6FF5B1">WWAN_GSM_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/62257D65-DCB9-43C3-A862-DAB31C27EF0A">WWAN_UMTS_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5D0DD219-8D81-4F72-B327-119A45CC35B4">WWAN_TDSCDMA_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/17A78DC7-A89D-405A-983E-FC0DC469A4B0">WWAN_LTE_SERVING_CELL_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ADEEB57F-79FF-4AA7-84AF-FED413E47057">WWAN_GSM_NMR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/B62F63EB-747A-4672-9A79-5065A8BC04D1">WWAN_UMTS_MRL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D919EF5E-502C-4983-AFC5-F3F6E6CC8C3B">WWAN_TDSCDMA_MRL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5959B7A7-147D-4F20-82CC-EC1DEAAE3494">WWAN_LTE_MRL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A19B98B5-F2E5-4AF9-9D2B-A7DD47441656">WWAN_CDMA_MRL</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_BASE_STATIONS_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
