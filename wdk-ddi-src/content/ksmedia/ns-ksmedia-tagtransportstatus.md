---
UID: NS.ksmedia.tagTRANSPORTSTATUS
title: tagTRANSPORTSTATUS
author: windows-driver-content
description: The TRANSPORTSTATUS structure describes the current transport status.
old-location: stream\transportstatus.htm
old-project: stream
ms.assetid: 2896fd39-5c33-4c79-8adb-f6862b7b4314
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagTRANSPORTSTATUS, TRANSPORTSTATUS, *PTRANSPORTSTATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSPORTSTATUS
req.alt-loc: ksmedia.h
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

# tagTRANSPORTSTATUS structure



## -description
<p>The TRANSPORTSTATUS structure describes the current transport status.</p>


## -syntax

````
typedef struct tagTRANSPORTSTATUS {
  LONG Mode;
  LONG LastError;
  LONG RecordInhibit;
  LONG ServoLock;
  LONG MediaPresent;
  LONG MediaLength;
  LONG MediaSize;
  LONG MediaTrackCount;
  LONG MediaTrackLength;
  LONG MediaTrackSide;
  LONG MediaType;
  LONG LinkMode;
  LONG NotifyOn;
} TRANSPORTSTATUS, *PTRANSPORTSTATUS;
````


## -struct-fields
<dl>

### -field <b>Mode</b>

<dd>
<p>Specifies the ED_MODE_Xxx.</p>
</dd>

### -field <b>LastError</b>

<dd>
<p>Specifies the last error.</p>
</dd>

### -field <b>RecordInhibit</b>

<dd>
<p>Specifies if recording is inhibited. <b>TRUE</b> if recording is prevented, <b>FALSE</b> otherwise.</p>
</dd>

### -field <b>ServoLock</b>

<dd>
<p>Indicates the servo lock.</p>
</dd>

### -field <b>MediaPresent</b>

<dd>
<p>Specifies if media is present.</p>
</dd>

### -field <b>MediaLength</b>

<dd>
<p>Specifies the length of the media.</p>
</dd>

### -field <b>MediaSize</b>

<dd>
<p>Specifies the size of the media.</p>
</dd>

### -field <b>MediaTrackCount</b>

<dd>
<p>Indicates the media track count.</p>
</dd>

### -field <b>MediaTrackLength</b>

<dd>
<p>Specifies the media track length.</p>
</dd>

### -field <b>MediaTrackSide</b>

<dd>
<p>Indicates the media track size.</p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>Indicates the type of media.</p>
</dd>

### -field <b>LinkMode</b>

<dd>
<p>Indicates linked mode. <b>TRUE</b> if linked, <b>FALSE</b> otherwise.</p>
</dd>

### -field <b>NotifyOn</b>

<dd>
<p>Specifies event notification. <b>TRUE</b> enables event notification, <b>FALSE</b> disables event notification.</p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>