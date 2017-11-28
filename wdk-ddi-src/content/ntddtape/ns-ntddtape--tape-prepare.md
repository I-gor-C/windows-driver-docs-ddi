---
UID: NS.ntddtape._TAPE_PREPARE
title: TAPE_PREPARE
author: windows-driver-content
description: The TAPE_PREPARE structure is used in conjunction with the IOCTL_TAPE_PREPARE request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape.
old-location: storage\tape_prepare.htm
old-project: storage
ms.assetid: 0bca5849-e0f9-42b2-82f8-aadea2aa01ae
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TAPE_PREPARE, TAPE_PREPARE, *PTAPE_PREPARE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddtape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_PREPARE
req.alt-loc: ntddtape.h
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

# TAPE_PREPARE structure



## -description
<p>The TAPE_PREPARE structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560630">IOCTL_TAPE_PREPARE</a> request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape.</p>


## -syntax

````
typedef struct _TAPE_PREPARE {
  ULONG   Operation;
  BOOLEAN Immediate;
} TAPE_PREPARE, *PTAPE_PREPARE;
````


## -struct-fields
<dl>

### -field <b>Operation</b>

<dd>
<p>Indicates the type of operation to perform. This member can be one of the following:</p>
<table>
<tr>
<th>Operation</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TAPE_LOAD</p>
</td>
<td>
<p>Loads the tape and moves the tape to the beginning. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_UNLOAD</p>
</td>
<td>
<p>Moves the tape to the beginning for removal from the device. After a successful unload operation, the device returns errors to applications that attempt to access the tape, until the tape is loaded again. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_TENSION</p>
</td>
<td>
<p>Adjusts the tension by moving the tape to the end of the tape and back to the beginning. This option is not supported by all devices. This value is ignored if it is not supported.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_LOCK</p>
</td>
<td>
<p>Locks the tape ejection mechanism, so that the tape is not ejected accidentally. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_UNLOCK</p>
</td>
<td>
<p>Unlocks the tape ejection mechanism. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_FORMAT</p>
</td>
<td>
<p>Performs a low-level format of the tape. Not all devices support this feature. This value is ignored if it is not supported.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Immediate</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that the target device should return status immediately. When set to <b>FALSE</b>, indicates that the device should return status after the operation is complete.</p>
</dd>
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
<dt>Ntddtape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560630">IOCTL_TAPE_PREPARE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567950">TapeMiniPrepare</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_PREPARE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
