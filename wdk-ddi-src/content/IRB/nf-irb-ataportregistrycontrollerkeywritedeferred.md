---
UID: NF.irb.AtaPortRegistryControllerKeyWriteDeferred
title: AtaPortRegistryControllerKeyWriteDeferred
author: windows-driver-content
description: The AtaPortRegistryControllerKeyWriteDeferred routine writes the data asynchronously to the indicated value name under the registry key HKLM\CurrentControlSet\Services\&lt;service name&gt;\ControllerN, where N is the number of the controller.
old-location: storage\ataportregistrycontrollerkeywritedeferred.htm
ms.assetid: f4297e91-06ae-4c7a-87bc-12e3f5b0238c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortRegistryControllerKeyWriteDeferred
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
ms.keywords: AtaPortRegistryControllerKeyWriteDeferred
req.iface: 
---

# AtaPortRegistryControllerKeyWriteDeferred function



## -description
<p>The <b>AtaPortRegistryControllerKeyWriteDeferred</b> routine writes the data asynchronously to the indicated value name under the registry key <b>HKLM\CurrentControlSet\Services\</b><i>&lt;service name&gt;</i><b>\Controller</b><i>N</i>, where <i>N </i>is the number of the controller. </p>


## -syntax

````
BOOLEAN __inline AtaPortRegistryControllerKeyWriteDeferred(
  _In_ PVOID  ChannelExtension,
  _In_ UCHAR  ControllerNumber,
  _In_ PCHAR  ValueName,
  _In_ UCHAR  ValueType,
  _In_ PUCHAR Buffer,
  _In_ PULONG Length
);
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension. </p>
</dd>

### -param <i>ControllerNumber</i> [in]

<dd>
<p>Contains the controller number. </p>
</dd>

### -param <i>ValueName</i> [in]

<dd>
<p>Contains the name of the registry value to write to. </p>
</dd>

### -param <i>ValueType</i> [in]

<dd>
<p>Indicates the type of data that is contained in the registry value. This member should be assigned one of values indicated in the following table. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>IDE_REG_DWORD</p>
</td>
<td>
<p>A 4-byte numeric value. </p>
</td>
</tr>
<tr>
<td>
<p>IDE_REG_BINARY</p>
</td>
<td>
<p>Binary data. </p>
</td>
</tr>
<tr>
<td>
<p>IDE_REG_SZ</p>
</td>
<td>
<p>A null-terminated, Unicode string. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the source buffer that contains the data to write to the registry value. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>A pointer to the number of bytes of data to copy. If the operation fails, the location pointed to by <i>Length</i> will update to the length of data that was successfully copied to the registry.</p>
</dd>
</dl>

## -returns
<p><b>AtaPortRegistryControllerKeyWriteDeferred</b> returns <b>TRUE</b> if the operation succeeds. Otherwise, it returns <b>FALSE</b>. The routine also returns <b>FALSE</b> if the miniport driver does not call it from the correct routine. </p>

## -remarks
<p>If the value name is not present, the <b>AtaPortRegistryControllerKeyWriteDeferred</b> routine creates an entry for the value name and stores the input data under the newly created value name. </p>

<p>The miniport driver can call the <b>AtaPortRegistryControllerKeyWriteDeferred</b> routine from any of the routines that are defined in the channel interface. </p>

<p>The buffer pointed to by <i>Buffer </i>must be allocated by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff550200">AtaPortRegistryAllocateBuffer</a>. The miniport driver must not reuse this buffer after it calls <b>AtaPortRegistryControllerKeyWriteDeferred</b> because the port driver delays writing the key data. If the miniport driver reuses the buffer, it might overwrite the data in the buffer before the port driver has an opportunity to store it in the registry key. The port driver flushes the buffer when the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a> to free the buffer. </p>

<p>If the value name is not present, the <b>AtaPortRegistryControllerKeyWriteDeferred</b> routine creates an entry for the value name and stores the input data under the newly created value name. </p>

<p>The miniport driver can call the <b>AtaPortRegistryControllerKeyWriteDeferred</b> routine from any of the routines that are defined in the channel interface. </p>

<p>The buffer pointed to by <i>Buffer </i>must be allocated by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff550200">AtaPortRegistryAllocateBuffer</a>. The miniport driver must not reuse this buffer after it calls <b>AtaPortRegistryControllerKeyWriteDeferred</b> because the port driver delays writing the key data. If the miniport driver reuses the buffer, it might overwrite the data in the buffer before the port driver has an opportunity to store it in the registry key. The port driver flushes the buffer when the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a> to free the buffer. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550200">AtaPortRegistryAllocateBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20AtaPortRegistryControllerKeyWriteDeferred routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
