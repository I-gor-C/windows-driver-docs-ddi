---
UID: NS.irb._IDE_CHANNEL_INTERFACE
title: IDE_CHANNEL_INTERFACE
author: windows-driver-content
description: The IDE_CHANNEL_INTERFACE structure contains interface information for the indicated channel.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_channel_interface.htm
old-project: storage
ms.assetid: 0a742dc2-fa1a-4b93-a136-52f4571bde22
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDE_CHANNEL_INTERFACE, IDE_CHANNEL_INTERFACE, *PIDE_CHANNEL_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_CHANNEL_INTERFACE
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

# IDE_CHANNEL_INTERFACE structure



## -description
<p>The IDE_CHANNEL_INTERFACE structure contains interface information for the indicated channel.</p>


## -syntax

````
typedef struct _IDE_CHANNEL_INTERFACE {
  USHORT            Version;
  UCHAR             ChannelNumber;
  UCHAR             Reserved;
  ULONG             ReservedUlong;
  IDE_HW_INITIALIZE IdeHwInitialize;
  IDE_HW_BUILDIO    IdeHwBuildIo;
  IDE_HW_STARTIO    IdeHwStartIo;
  IDE_HW_INTERRUPT  IdeHwInterrupt;
  IDE_HW_RESET      IdeHwReset;
  IDE_HW_CONTROL    IdeHwControl;
} IDE_CHANNEL_INTERFACE, *PIDE_CHANNEL_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The port driver sets this member to sizeof(IDE_CHANNEL_INTERFACE). The miniport driver should verify that the version is greater than or equal to the one it is using.</p>
</dd>

### -field <b>ChannelNumber</b>

<dd>
<p>The port driver sets this field to the number assigned for this channel. For non-native mode controllers, the primary channel will always be assigned 0 and the secondary channel will always be assigned 1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. The miniport driver must not use this field.</p>
</dd>

### -field <b>ReservedUlong</b>

<dd>
<dl>


</dl>
</dd>

### -field <b>IdeHwInitialize</b>

<dd></dd>

### -field <b>IdeHwBuildIo</b>

<dd></dd>

### -field <b>IdeHwStartIo</b>

<dd></dd>

### -field <b>IdeHwInterrupt</b>

<dd></dd>

### -field <b>IdeHwReset</b>

<dd></dd>

### -field <b>IdeHwControl</b>

<dd></dd>
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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.idehwinitialize">IdeHwInitialize</a>
</dt>
<dt>
<a href="storage.idehwbuildio">IdeHwBuildIo</a>
</dt>
<dt>
<a href="storage.idehwstartio">IdeHwStartIo</a>
</dt>
<dt>
<a href="storage.idehwinterrupt">IdeHwInterrupt</a>
</dt>
<dt>
<a href="storage.idehwreset">IdeHwReset</a>
</dt>
<dt>
<a href="storage.idehwcontrol">IdeHwControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IDE_CHANNEL_INTERFACE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
