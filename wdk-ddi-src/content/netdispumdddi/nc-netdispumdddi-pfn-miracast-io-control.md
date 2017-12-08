---
UID: NC.netdispumdddi.PFN_MIRACAST_IO_CONTROL
title: PFN_MIRACAST_IO_CONTROL
author: windows-driver-content
description: Called by the user-mode display driver to send the kernel-mode display miniport driver a synchronous I/O control request.The data type of this function is PFN_MIRACAST_IO_CONTROL.
old-location: display\miracastiocontrol.htm
old-project: display
ms.assetid: df63ec18-79e0-40a6-a412-46071eb8a7fe
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiracastIoControl
req.alt-loc: Netdispumdddi.h
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

# PFN_MIRACAST_IO_CONTROL callback



## -description
<p>Called by the user-mode display driver to send the kernel-mode  display miniport driver a synchronous I/O control request.<p>The data type of this function is <b>PFN_MIRACAST_IO_CONTROL</b>.</p>
</p>
<p>The data type of this function is <b>PFN_MIRACAST_IO_CONTROL</b>.</p>


## -prototype

````
PFN_MIRACAST_IO_CONTROL MiracastIoControl;

NTSTATUS MiracastIoControl(
  _In_      HANDLE hMiracastDeviceHandle,
  _In_      BOOL   HardwareAccess,
  _In_      UINT   InputBufferSize,
  _In_      VOID   *pInputBuffer,
  _In_      UINT   OutputBufferSize,
  _Out_     VOID   *pOutputBuffer,
  _Out_opt_ UINT   *pBytesReturned
)
{ ... }
````


## -parameters
<dl>

### -param hMiracastDeviceHandle [in]

<dd>
<p>A handle that represents a Miracast device. The Miracast user-mode driver previously obtained this handle as the <i>hMiracastDeviceHandle</i> parameter in a call to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> function.</p>
</dd>

### -param HardwareAccess [in]

<dd>
<p>A Boolean value that indicates whether this I/O control request from the user-mode display driver needs to flush all the pending GPU DMA buffers.</p>
<p>We don't recommend that the driver set this value to <b>TRUE</b> except when necessary, because flushing the GPU will create substantial processing overhead.</p>
</dd>

### -param InputBufferSize [in]

<dd>
<p>The size, in bytes, of the input buffer pointed to by <i>pInputBuffer</i>.</p>
</dd>

### -param pInputBuffer [in]

<dd>
<p>A pointer to the input buffer. The <i>InputBufferSize</i> parameter specifies the size of the buffer.</p>
</dd>

### -param OutputBufferSize [in]

<dd>
<p>The size, in bytes, of the output buffer pointed to by <i>pOutputBuffer</i>.</p>
</dd>

### -param pOutputBuffer [out]

<dd>
<p>A driver-supplied pointer to the output buffer. The <i>OutputBufferSize</i> parameter specifies the size of the buffer.</p>
</dd>

### -param pBytesReturned [out, optional]

<dd>
<p>An optional driver-supplied pointer to a <b>UINT</b>-type variable that holds the number of bytes that the display miniport driver returned.</p>
</dd>
</dl>

## -returns
<p>On success, the operating system returns <b>STATUS_SUCCESS</b>. Otherwise, the function returns an error code defined in the Ntstatus.h header.</p>

## -remarks
<p>If the Miracast user-mode driver calls <b>MiracastIoControl</b> when the operating system is starting a Miracast session, and if the calling thread is not the thread in which the operating system calls the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a> function, the operating system blocks the <b>MiracastIoControl</b> call until the Miracast start session is finished. If the user-mode driver calls <b>MiracastIoControl</b> in the same context as is used in  the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> or <i>StartMiracastSession</i> functions, the operating system will process the call.</p>

<p>If the Miracast user-mode driver calls <b>MiracastIoControl</b> when the operating system is stopping a Miracast session, and if the calling thread is not the thread in which the operating system calls the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> function, the operating system will fail this call. If the user-mode driver calls <b>MiracastIoControl</b> in the same context as is used in  the <i>StopMiracastSession</i> or <a href="..\netdispumdddi\nc-netdispumdddi-pfn-destroy-miracast-context.md">DestroyMiracastContext</a> functions, the operating system will process the call.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-destroy-miracast-context.md">DestroyMiracastContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_MIRACAST_IO_CONTROL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
