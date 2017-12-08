---
UID: NS.dispmprt._DXGK_TIMED_OPERATION
title: DXGK_TIMED_OPERATION
author: windows-driver-content
description: The DXGK_TIMED_OPERATION structure describes a timed operation, which is used in the Timed Operation Interface.
old-location: display\dxgk_timed_operation.htm
old-project: display
ms.assetid: 6b377ba5-cd3b-433e-bd9c-315203c3bc69
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_TIMED_OPERATION, DXGK_TIMED_OPERATION, *PDXGK_TIMED_OPERATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_TIMED_OPERATION
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_TIMED_OPERATION structure



## -description
<p>The DXGK_TIMED_OPERATION structure describes a timed operation, which is used in the <a href="display.timed_operation_interface">Timed Operation Interface</a>.</p>


## -syntax

````
typedef struct _DXGK_TIMED_OPERATION {
  USHORT        Size;
  ULONG_PTR     OwnerTag;
  BOOLEAN       OsHandled;
  BOOLEAN       TimeoutTriggered;
  LARGE_INTEGER Timeout;
  LARGE_INTEGER StartTick;
} DXGK_TIMED_OPERATION, *PDXGK_TIMED_OPERATION;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>[in] The size, in bytes, of this structure.</p>
</dd>

### -field OwnerTag

<dd>
<p>[system] A pointer to the place in the code that started the timed operation.</p>
</dd>

### -field OsHandled

<dd>
<p>[system] For system use only. </p>
</dd>

### -field TimeoutTriggered

<dd>
<p>[out] A Boolean value that specifies whether the time-out was triggered. </p>
</dd>

### -field Timeout

<dd>
<p>[system] For system use only. </p>
</dd>

### -field StartTick

<dd>
<p>[system] For system use only. </p>
</dd>
</dl>

## -remarks
<p>Display miniport drivers should not change of rely on members that are marked with the  [system] designation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.timed_operation_interface">Timed Operation Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_TIMED_OPERATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
