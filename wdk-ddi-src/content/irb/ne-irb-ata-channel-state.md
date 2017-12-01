---
UID: NE.irb.ATA_CHANNEL_STATE
title: ATA_CHANNEL_STATE
author: windows-driver-content
description: The ATA_CHANNEL_STATE enumeration type indicates the state of the channel.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ata_channel_state.htm
old-project: storage
ms.assetid: 97df2db8-6a42-46d4-bc31-babb124635ee
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: WdmlibIoGetAffinityInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATA_CHANNEL_STATE
req.alt-loc: irb.h
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
---

# ATA_CHANNEL_STATE enumeration



## -description
<p>The ATA_CHANNEL_STATE enumeration type indicates the state of the channel.</p>


## -syntax

````
typedef enum  { 
  ChannelStateDisabled  = 0,
  ChannelStateEnabled   = 1,
  ChannelStateUnKnown   = 2
} ATA_CHANNEL_STATE;
````


## -enum-fields
<dl>

### -field <a id="ChannelStateDisabled"></a><a id="channelstatedisabled"></a><a id="CHANNELSTATEDISABLED"></a><b>ChannelStateDisabled</b>

<dd>
<p>Indicates that the channel is disabled.</p>
</dd>

### -field <a id="ChannelStateEnabled"></a><a id="channelstateenabled"></a><a id="CHANNELSTATEENABLED"></a><b>ChannelStateEnabled</b>

<dd>
<p>Indicates that the channel is enabled.</p>
</dd>

### -field <a id="ChannelStateUnKnown"></a><a id="channelstateunknown"></a><a id="CHANNELSTATEUNKNOWN"></a><b>ChannelStateUnKnown</b>

<dd>
<p>Indicates that the state of the channel is unknown.</p>
</dd>
</dl>

## -remarks
<p>The ATA_CHANNEL_STATE enumeration type is used in conjunction with the <a href="storage.atacontrollerchannelenabled">AtaControllerChannelEnabled</a> routine to determine whether the channel is enabled.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.atacontrollerchannelenabled">AtaControllerChannelEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ATA_CHANNEL_STATE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
