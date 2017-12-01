---
UID: NS.windot11._DOT11_MAC_PARAMETERS
title: DOT11_MAC_PARAMETERS
author: windows-driver-content
description: The DOT11_MAC_PARAMETERS is the optional input for an OID_DOT11_CREATE_MAC request. The device role is defined in an operation mode bitmask included in this structure.
old-location: netvista\dot11_mac_parameters.htm
old-project: netvista
ms.assetid: 53114ABE-33F2-4DA2-ABE0-2547547AA6AD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_MAC_PARAMETERS, DOT11_MAC_PARAMETERS, *PDOT11_MAC_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_MAC_PARAMETERS
req.alt-loc: Windot11.h
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_MAC_PARAMETERS structure



## -description

## -syntax

````
typedef struct _DOT11_MAC_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              uOpmodeMask;
} DOT11_MAC_PARAMETERS, *PDOT11_MAC_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The object header identifying the type and revision of this structure. The required member settings of <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> are the following:</p>
<dl class="indent">

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><p><a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b></p>


<dd>
<p>Must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b></p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><p><a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b></p>


<dd>
<p>Must be set to <b>DOT11_MAC_PARAMETERS_REVISION_1</b></p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><p><a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b></p>


<dd>
<p>Must be set to <b>DOT11_SIZEOF_MAC_PARAMETERS_REVISION_1</b></p>
</dd>
</dl>
</dd>

### -field <b>uOpmodeMask</b>

<dd>
<p>A bitwise OR value of the operation modes Windows may set for the created port. This bitmask is defined through the following:</p>
<p></p>
<dl>

### -field <a id="DOT11_OPERATION_MODE_WFD_DEVICE"></a><a id="dot11_operation_mode_wfd_device"></a>DOT11_OPERATION_MODE_WFD_DEVICE

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Device operation mode.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_WFD_GROUP_OWNER"></a><a id="dot11_operation_mode_wfd_group_owner"></a>DOT11_OPERATION_MODE_WFD_GROUP_OWNER

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Group Owner operation mode.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_WFD_CLIENT"></a><a id="dot11_operation_mode_wfd_client"></a>DOT11_OPERATION_MODE_WFD_CLIENT

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Client operation mode.</p>
</dd>
</dl>
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
<p>Versions: Supported in Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569124">OID_DOT11_CREATE_MAC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_MAC_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
