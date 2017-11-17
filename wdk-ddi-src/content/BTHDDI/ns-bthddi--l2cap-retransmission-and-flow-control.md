---
UID: NS.bthddi._L2CAP_RETRANSMISSION_AND_FLOW_CONTROL
title: L2CAP_RETRANSMISSION_AND_FLOW_CONTROL
author: windows-driver-content
description: The L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure describes configuration parameters for enhanced retransmission mode and streaming mode.
old-location: bltooth\l2cap_retransmission_and_flow_control.htm
ms.assetid: 0D4528C0-AEE6-4AD2-A3E6-524A6EB8A0D9
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
req.alt-api: L2CAP_RETRANSMISSION_AND_FLOW_CONTROL
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
ms.keywords: L2CAP_RETRANSMISSION_AND_FLOW_CONTROL, L2CAP_RETRANSMISSION_AND_FLOW_CONTROL, *PL2CAP_RETRANSMISSION_AND_FLOW_CONTROL
req.iface: IBidiSpl2
---

# L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure



## -description
<p>The L2CAP_RETRANSMISSION_AND_FLOW_CONTROL structure describes configuration parameters for enhanced retransmission mode and streaming mode.</p>


## -syntax

````
typedef struct _L2CAP_RETRANSMISSION_AND_FLOW_CONTROL {
  UCHAR  Mode;
  UCHAR  TxWindowSize;
  UCHAR  MaxTransmit;
  USHORT RetransmissionTO;
  USHORT MonitorTO;
  USHORT MaxPDUSize;
} L2CAP_RETRANSMISSION_AND_FLOW_CONTROL, *PL2CAP_RETRANSMISSION_AND_FLOW_CONTROL;
````


## -struct-fields
<dl>

### -field <b>Mode</b>

<dd>
<p>Requested mode for the enhanced L2CAP channel.</p>
</dd>

### -field <b>TxWindowSize</b>

<dd>
<p>Size of the transmission window for enhanced retransmission mode. The value of member is valid only when used with enhanced retransmission mode, and is ignored in streaming mode. Valid values range from 1 to 63.</p>
</dd>

### -field <b>MaxTransmit</b>

<dd>
<p>Number of times a single I/S frame will be re-transmitted in case of an error. The value of this member is valid only for enhanced retransmission mode and is ignored in streaming mode. The minimum value is 1.</p>
</dd>

### -field <b>RetransmissionTO</b>

<dd>
<p>Retransmission timeout value. Profile drivers should set this value to 0.</p>
</dd>

### -field <b>MonitorTO</b>

<dd>
<p>Monitor timeout. Profile drivers should set this value to 0.</p>
</dd>

### -field <b>MaxPDUSize</b>

<dd>
<p>Maximum PDU Size.</p>
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