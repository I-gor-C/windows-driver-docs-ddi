---
UID: NS.bthddi._CHANNEL_CONFIG_PARAMETERS
title: CHANNEL_CONFIG_PARAMETERS
author: windows-driver-content
description: The CHANNEL_CONFIG_PARAMETERS structure contains configuration parameters for inbound and outbound directions of a L2CAP channel.
old-location: bltooth\channel_config_parameters.htm
old-project: bltooth
ms.assetid: c2201e3c-c680-4a22-adf5-5131fb138066
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: CHANNEL_CONFIG_PARAMETERS, CHANNEL_CONFIG_PARAMETERS, *PCHANNEL_CONFIG_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANNEL_CONFIG_PARAMETERS
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.iface: IBidiSpl2
---

# CHANNEL_CONFIG_PARAMETERS structure



## -description
<p>The CHANNEL_CONFIG_PARAMETERS structure contains configuration parameters for inbound and outbound
  directions of a L2CAP channel.</p>


## -syntax

````
typedef struct _CHANNEL_CONFIG_PARAMETERS {
  ULONG                Flags;
  CO_MTU               Mtu;
  CO_FLUSHTO           FlushTO;
  ULONG                NumExtraOptions;
  PL2CAP_CONFIG_OPTION ExtraOptions;
  L2CAP_FLOWSPEC       Flow;
} CHANNEL_CONFIG_PARAMETERS, *PCHANNEL_CONFIG_PARAMETERS;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>A flag or combination of flags that specifies which members of this structure contain data. Valid
     flag values are listed in the following table.
     </p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>CFG_EXTRA</p>
</td>
<td>
<p>If set, the 
        <b>ExtraOptions</b> member contains data.</p>
</td>
</tr>
<tr>
<td>
<p>CFG_FLUSHTO</p>
</td>
<td>
<p>If set, the 
        <b>FlushTO</b> member contains data.</p>
</td>
</tr>
<tr>
<td>
<p>CFG_MTU</p>
</td>
<td>
<p>If set, the 
        <b>Mtu</b> member contains data.</p>
</td>
</tr>
<tr>
<td>
<p>CFG_QOS</p>
</td>
<td>
<p>If set, the 
        <b>Flow</b> member contains data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Mtu

<dd>
<p>The message transfer units for the specified channel direction.</p>
</dd>

### -field FlushTO

<dd>
<p>The flush timeout for the specified channel direction.</p>
</dd>

### -field NumExtraOptions

<dd>
<p>The number of items specified in the array that is specified in the 
     <b>ExtraOptions</b> member.</p>
</dd>

### -field ExtraOptions

<dd>
<p>The number of items specified in the array that is specified in the 
     <b>ExtraOptions</b> member.</p>
</dd>

### -field Flow

<dd>
<p>The QoS settings for the specified channel direction.</p>
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
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bthddi\ns-bthddi--l2cap-config-option.md">L2CAP_CONFIG_OPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20CHANNEL_CONFIG_PARAMETERS structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
