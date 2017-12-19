---
UID: NF.video.VideoPortLockBuffer
title: VideoPortLockBuffer function
author: windows-driver-content
description: The VideoPortLockBuffer function probes the specified buffer, makes the buffer's memory pages resident in memory, and locks the physical pages mapped by the virtual address range.
old-location: display\videoportlockbuffer.htm
old-project: display
ms.assetid: ba65d1b1-a720-4f21-8c6d-af70185c0c24
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: VideoPortLockBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortLockBuffer
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# VideoPortLockBuffer function



## -description
The <b>VideoPortLockBuffer</b> function probes the specified buffer, makes the buffer's memory pages resident in memory, and locks the physical pages mapped by the virtual address range.



## -syntax

````
PVOID VideoPortLockBuffer(
  _In_ PVOID             HwDeviceExtension,
  _In_ PVOID             BaseAddress,
  _In_ ULONG             Length,
  _In_ VP_LOCK_OPERATION Operation
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the miniport driver's device extension.


### -param BaseAddress [in]

Specifies the virtual address of the buffer to be locked.


### -param Length [in]

Specifies the length in bytes of the buffer to be locked.


### -param Operation [in]

Specifies the type of operation for which the caller wants the access rights probed and the pages locked. The operation can be one of the following: <b>VpReadAccess</b>, <b>VpWriteAccess</b>, or <b>VpModifyAccess</b>.


## -returns
Returns a pointer to a memory descriptor list (<a href="wdkgloss.m#wdkgloss.mdl#wdkgloss.mdl"><i>MDL</i></a>), or a <b>NULL</b> pointer if the MDL for the memory to be locked cannot be allocated.


## -remarks
To unlock the buffer, the video miniport driver should call <a href="display.videoportunlockbuffer">VideoPortUnlockBuffer</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows XP and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.videoportunlockbuffer">VideoPortUnlockBuffer</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortLockBuffer function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

