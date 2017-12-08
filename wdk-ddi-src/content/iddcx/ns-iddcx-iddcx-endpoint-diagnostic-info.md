---
UID: NS.iddcx.IDDCX_ENDPOINT_DIAGNOSTIC_INFO
title: IDDCX_ENDPOINT_DIAGNOSTIC_INFO
author: windows-driver-content
description: Gives information about the video data endpoint.
old-location: display\iddcx_endpoint_diagnostic_info.htm
old-project: display
ms.assetid: 70be09ed-5633-464b-b311-f671efe83a54
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_ENDPOINT_DIAGNOSTIC_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_ENDPOINT_DIAGNOSTIC_INFO
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_ENDPOINT_DIAGNOSTIC_INFO structure



## -description
<p>Gives information about the video data endpoint.</p>


## -syntax

````
typedef struct IDDCX_ENDPOINT_DIAGNOSTIC_INFO {
  UINT                         Size;
  IDDCX_TRANSMISSION_TYPE      TransmissionType;
  PCWSTR                       pEndPointFriendlyName;
  PCWSTR                       pEndPointModelName;
  PCWSTR                       pEndPointManufacturerName;
  IDDCX_ENDPOINT_VERSION*      pHardwareVersion;
  IDDCX_ENDPOINT_VERSION*      pFirmwareVersion;
  IDDCX_FEATURE_IMPLEMENTATION GammaSupport;
} IDDCX_ENDPOINT_DIAGNOSTIC_INFO, *IDDCX_ENDPOINT_DIAGNOSTIC_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     
                 Total size of the structure.</p>
</dd>

### -field TransmissionType

<dd>
<p>
                     Describes the type of link the video data is being transmitted over.
                 </p>
</dd>

### -field pEndPointFriendlyName

<dd>
<p>
                     The friendly name of the endpoint, if one exists. This is applicable if the user can give the device a name and is NULL if a friendly name does not exist.
                 </p>
</dd>

### -field pEndPointModelName

<dd>
<p>
                     The model name of the endpoint. Must be a non-empty string.
                 </p>
</dd>

### -field pEndPointManufacturerName

<dd>
<p>
                     The manufacture name of the endpoint. Must be a non-empty string.
                 </p>
</dd>

### -field pHardwareVersion

<dd>
<p>
                     Pointer to version info for the endpoint hardware.
                 </p>
</dd>

### -field pFirmwareVersion

<dd>
<p>
                     Pointer to version info for the endpoint firmware.
                 </p>
</dd>

### -field GammaSupport

<dd>
<p>
                     Indicates how gamma is implemented.
                 </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>