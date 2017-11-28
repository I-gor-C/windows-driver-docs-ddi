---
UID: NE.ntddndis._NDIS_PROCESSOR_VENDOR
title: NDIS_PROCESSOR_VENDOR
author: windows-driver-content
description: The NDIS_PROCESSOR_VENDOR enumeration identifies a processor vendor.
old-location: netvista\ndis_processor_vendor.htm
old-project: netvista
ms.assetid: c2d1b967-32fb-437a-a0bd-e0028acee022
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PROCESSOR_VENDOR
req.alt-loc: ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_PROCESSOR_VENDOR enumeration



## -description
<p>The NDIS_PROCESSOR_VENDOR enumeration identifies a processor vendor.</p>


## -syntax

````
typedef enum _NDIS_PROCESSOR_VENDOR { 
  NdisProcessorVendorUnknown,
  NdisProcessorVendorGenuinIntel,
  NdisProcessorVendorAuthenticAMD
} NDIS_PROCESSOR_VENDOR, *PNDIS_PROCESSOR_VENDOR;
````


## -enum-fields
<dl>

### -field <a id="NdisProcessorVendorUnknown"></a><a id="ndisprocessorvendorunknown"></a><a id="NDISPROCESSORVENDORUNKNOWN"></a><b>NdisProcessorVendorUnknown</b>

<dd>
<p>The processor vendor is unknown.</p>
</dd>

### -field <a id="NdisProcessorVendorGenuinIntel"></a><a id="ndisprocessorvendorgenuinintel"></a><a id="NDISPROCESSORVENDORGENUININTEL"></a><b>NdisProcessorVendorGenuinIntel</b>

<dd>
<p>The processor vendor is Intel.</p>
</dd>

### -field <a id="NdisProcessorVendorAuthenticAMD"></a><a id="ndisprocessorvendorauthenticamd"></a><a id="NDISPROCESSORVENDORAUTHENTICAMD"></a><b>NdisProcessorVendorAuthenticAMD</b>

<dd>
<p>The processor vendor is AMD.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PROCESSOR_VENDOR enumeration is used in the 
    <a href="..\ndis\ns-ndis--ndis-system-processor-info.md">
    NDIS_SYSTEM_PROCESSOR_INFO</a> structure.</p>

<p>The NDIS_PROCESSOR_VENDOR enumeration is used in the 
    <a href="..\ndis\ns-ndis--ndis-system-processor-info.md">
    NDIS_SYSTEM_PROCESSOR_INFO</a> structure.</p>

<p>The NDIS_PROCESSOR_VENDOR enumeration is used in the 
    <a href="..\ndis\ns-ndis--ndis-system-processor-info.md">
    NDIS_SYSTEM_PROCESSOR_INFO</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567871">NDIS_SYSTEM_PROCESSOR_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROCESSOR_VENDOR enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
