---
UID: NS.1394._SELF_ID
title: SELF_ID
author: windows-driver-content
description: The SELF_ID structure contains a raw packet zero self-ID packet. See the IEEE 1394 Trade Association specification website for details.
old-location: ieee\self_id.htm
old-project: IEEE
ms.assetid: c168ca19-e4a7-484d-8aed-0b7e7033b760
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: SELF_ID, SELF_ID, *PSELF_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SELF_ID
req.alt-loc: 1394.h
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
---

# SELF_ID structure



## -description
<p>The SELF_ID structure contains a raw packet zero self-ID packet. See the <a href="http://go.microsoft.com/fwlink/p/?linkid=8729">IEEE 1394 Trade Association specification</a> website for details.</p>


## -syntax

````
typedef struct _SELF_ID {
  ULONG SID_Phys_ID  :6;
  ULONG SID_Packet_ID  :2;
  ULONG SID_Gap_Count  :6;
  ULONG SID_Link_Active  :1;
  ULONG SID_Zero  :1;
  ULONG SID_Power_Class  :3;
  ULONG SID_Contender  :1;
  ULONG SID_Delay  :2;
  ULONG SID_Speed  :2;
  ULONG SID_More_Packets  :1;
  ULONG SID_Initiated_Rst  :1;
  ULONG SID_Port3  :2;
  ULONG SID_Port2  :2;
  ULONG SID_Port1  :2;
} SELF_ID, *PSELF_ID;
````


## -struct-fields
<dl>

### -field SID_Phys_ID

<dd>
<p>Specifies the device node number. This member contains bits 0-5 of byte 0 of the self-ID packet. </p>
</dd>

### -field SID_Packet_ID

<dd>
<p>Must be PHY_PACKET_ID_SELF_ID. This member contains bits 6-7 of byte 0 of the self-ID packet. </p>
</dd>

### -field SID_Gap_Count

<dd>
<p>Specifies the current value of the node's PHY_CONFIGURATION register's gap_count member. This member contains bits 0-5 of byte 1 of the self-ID packet. </p>
</dd>

### -field SID_Link_Active

<dd>
<p>One if the device's link and transaction layers are active, zero otherwise. This member contains bit 6 of byte 1 of the self-ID packet. </p>
</dd>

### -field SID_Zero

<dd>
<p>Always zero. This member contains bit 7 of byte 1 of the self-ID packet. </p>
</dd>

### -field SID_Power_Class

<dd>
<p>The possible power classes are:</p>
<dl>
<dd>
<p>POWER_CLASS_NOT_NEED_NOT_REPEAT</p>
</dd>
<dd>
<p>POWER_CLASS_SELF_POWER_PROVIDE_15W</p>
</dd>
<dd>
<p>POWER_CLASS_SELF_POWER_PROVIDE_30W</p>
</dd>
<dd>
<p>POWER_CLASS_SELF_POWER_PROVIDE_45W</p>
</dd>
<dd>
<p>POWER_CLASS_MAYBE_POWERED_UPTO_1W</p>
</dd>
<dd>
<p>POWER_CLASS_IS_POWERED_UPTO_1W_NEEDS_2W</p>
</dd>
<dd>
<p>POWER_CLASS_IS_POWERED_UPTO_1W_NEEDS_5W</p>
</dd>
<dd>
<p>POWER_CLASS_IS_POWERED_UPTO_1W_NEEDS_9W</p>
</dd>
</dl>
<p>This member contains bits 0-2 of byte 2 of the self-ID packet. </p>
</dd>

### -field SID_Contender

<dd>
<p>One if this node is a contender for bus or isochronous resource manager, zero otherwise. This member contains bit 3 of byte 2 of the self-ID packet. </p>
</dd>

### -field SID_Delay

<dd>
<p>Currently always zero. This member contains bits 4-5 of byte 2 of the self-ID packet. </p>
</dd>

### -field SID_Speed

<dd>
<p>Specifies the maximum data transfer rate that is supported by the node. This member must have one of the values specified in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Speed</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>S100 speed</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>S200 speed</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>S400 speed</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Reserved (generally treated as S400/S800 speed)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field SID_More_Packets

<dd>
<p>One if this packet will be followed by SELF_ID_MORE packets, zero otherwise. This member contains bit 0 of byte 3 of the self-ID packet. </p>
</dd>

### -field SID_Initiated_Rst

<dd>
<p>One if this node initiated the most recent bus reset, zero otherwise. This member contains bit 1 of byte 3 of the self-ID packet. </p>
</dd>

### -field SID_Port3

<dd>
<p>Byte 3 - Bits 2-3</p>
</dd>

### -field SID_Port2

<dd>
<p>Byte 3 - Bits 4-5</p>
</dd>

### -field SID_Port1

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>Member <b>SID_Port1</b> contains bits 2-3 of byte 3 of the self-ID packet. Member <b>SID_Port2</b> contains bits 4-5 of byte 3 of the self-ID packet. Member <b>SID_Port3</b> contains bits 6-7 of byte 3 of the self-ID packet. </p>
</dd>
</dl>

## -remarks
<p>This structure corresponds to self ID packet 0, as described in the <i>P1394a</i> specification.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538877">TOPOLOGY_MAP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20SELF_ID structure%20 RELEASE:%20(11/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
