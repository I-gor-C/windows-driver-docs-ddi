---
UID: NS.bthddi._CHANNEL_CONFIG_PARAMETERS_ENHANCED
title: CHANNEL_CONFIG_PARAMETERS_ENHANCED
author: windows-driver-content
description: The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel.
old-location: bltooth\channel_config_parameters_enhanced.htm
ms.assetid: 4C28FD6E-A1DD-4887-95B0-6028ECA18204
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: bltooth
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8 and later versions of Windows
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANNEL_CONFIG_PARAMETERS_ENHANCED
req.alt-loc: Bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback
   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access
   paged memory)
ms.keywords: CHANNEL_CONFIG_PARAMETERS_ENHANCED, CHANNEL_CONFIG_PARAMETERS_ENHANCED, *PCHANNEL_CONFIG_PARAMETERS_ENHANCED
req.iface: IBidiSpl2
---

# CHANNEL_CONFIG_PARAMETERS_ENHANCED structure



## -description
<p>The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel.</p>


## -syntax

````
typedef struct _CHANNEL_CONFIG_PARAMETERS_ENHANCED {
  ULONG                                 Flags;
  CO_MTU                                Mtu;
  CO_FLUSHTO                            FlushTO;
  ULONG                                 NumExtraOptions;
  PL2CAP_CONFIG_OPTION                  ExtraOptions;
  L2CAP_FLOWSPEC                        Flow;
  L2CAP_RETRANSMISSION_AND_FLOW_CONTROL RetransmissionAndFlow;
  CO_FCS                                Fcs;
  L2CAP_EXTENDED_FLOW_SPEC              ExtendedFlowSpec;
  CO_EXTENDED_WINDOW_SIZE               ExtendedWindowSize;
} CHANNEL_CONFIG_PARAMETERS_ENHANCED, *PCHANNEL_CONFIG_PARAMETERS_ENHANCED;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Combination of CFG_XXX flags.</p>
</dd>

### -field <b>Mtu</b>

<dd>
<p>MTU for the direction.</p>
</dd>

### -field <b>FlushTO</b>

<dd>
<p>Flush timeout for the direction</p>
</dd>

### -field <b>NumExtraOptions</b>

<dd>
<p>Number of elements in the ExtraOptions array</p>
</dd>

### -field <b>ExtraOptions</b>

<dd>
<p>Array of extra options</p>
</dd>

### -field <b>Flow</b>

<dd>
<p>QOS for the direction</p>
</dd>

### -field <b>RetransmissionAndFlow</b>

<dd>
<p>Retransmission and flow for the direction</p>
</dd>

### -field <b>Fcs</b>

<dd>
<p>Frame check sequence</p>
</dd>

### -field <b>ExtendedFlowSpec</b>

<dd>
<p>Extended flow specification for the L2CAP channel. This member is reserved. Do not use.</p>
</dd>

### -field <b>ExtendedWindowSize</b>

<dd>
<p>Extended window size. This member is reserved. Do not use.</p>
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
<p>Versions: Supported in Windows 8 and later versions of Windows</p>
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