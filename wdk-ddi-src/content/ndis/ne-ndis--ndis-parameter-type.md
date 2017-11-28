---
UID: NE.ndis._NDIS_PARAMETER_TYPE
title: NDIS_PARAMETER_TYPE
author: windows-driver-content
description: The NDIS_PARAMETER_TYPE enumeration type identifies the type of a registry entry.
old-location: netvista\ndis_parameter_type.htm
old-project: netvista
ms.assetid: f17e390a-fa13-4435-ad1e-3fecc035ec41
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS
   5.1 drivers in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PARAMETER_TYPE
req.alt-loc: ndis.h
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

# NDIS_PARAMETER_TYPE enumeration



## -description
<p>The NDIS_PARAMETER_TYPE enumeration type identifies the type of a registry entry.</p>


## -syntax

````
typedef enum _NDIS_PARAMETER_TYPE { 
  NdisParameterInteger,
  NdisParameterHexInteger,
  NdisParameterString,
  NdisParameterMultiString,
  NdisParameterBinary
} NDIS_PARAMETER_TYPE, *PNDIS_PARAMETER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisParameterInteger"></a><a id="ndisparameterinteger"></a><a id="NDISPARAMETERINTEGER"></a><b>NdisParameterInteger</b>

<dd>
<p>An integer in decimal notation.</p>
</dd>

### -field <a id="NdisParameterHexInteger"></a><a id="ndisparameterhexinteger"></a><a id="NDISPARAMETERHEXINTEGER"></a><b>NdisParameterHexInteger</b>

<dd>
<p>An integer in hexadecimal notation.</p>
</dd>

### -field <a id="NdisParameterString"></a><a id="ndisparameterstring"></a><a id="NDISPARAMETERSTRING"></a><b>NdisParameterString</b>

<dd>
<p>A string of type NDIS_STRING.</p>
</dd>

### -field <a id="NdisParameterMultiString"></a><a id="ndisparametermultistring"></a><a id="NDISPARAMETERMULTISTRING"></a><b>NdisParameterMultiString</b>

<dd>
<p>A multistring parameter of the REG_MULTI_SZ type.</p>
</dd>

### -field <a id="NdisParameterBinary"></a><a id="ndisparameterbinary"></a><a id="NDISPARAMETERBINARY"></a><b>NdisParameterBinary</b>

<dd>
<p>A binary value of type REG_BINARY.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PARAMETER_TYPE enumeration type is used in the 
    <a href="..\ndis\ns-ndis--ndis-configuration-parameter.md">
    NDIS_CONFIGURATION_PARAMETER</a> structure and in the 
    <i>ParameterType</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a> function.</p>

<p>The NDIS_PARAMETER_TYPE enumeration type is used in the 
    <a href="..\ndis\ns-ndis--ndis-configuration-parameter.md">
    NDIS_CONFIGURATION_PARAMETER</a> structure and in the 
    <i>ParameterType</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a> function.</p>

<p>The NDIS_PARAMETER_TYPE enumeration type is used in the 
    <a href="..\ndis\ns-ndis--ndis-configuration-parameter.md">
    NDIS_CONFIGURATION_PARAMETER</a> structure and in the 
    <i>ParameterType</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS
   5.1 drivers in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564868">NDIS_CONFIGURATION_PARAMETER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PARAMETER_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
