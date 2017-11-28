---
UID: NS.avcstrm._AVC_STREAM_REQUEST_BLOCK
title: AVC_STREAM_REQUEST_BLOCK
author: windows-driver-content
description: The AVC_STREAM_REQUEST_BLOCK structure describes an AV/C streaming request to be processed by avcstrm.sys.
old-location: stream\avc_stream_request_block.htm
old-project: stream
ms.assetid: 077fc4ab-94a0-42eb-a0c5-684e447cb038
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: AVC_STREAM_REQUEST_BLOCK, AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: avcstrm.h
req.include-header: Avcstrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVC_STREAM_REQUEST_BLOCK
req.alt-loc: avcstrm.h
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

# AVC_STREAM_REQUEST_BLOCK structure



## -description
<p>The AVC_STREAM_REQUEST_BLOCK structure describes an AV/C streaming request to be processed by <i>avcstrm.sys</i>.</p>


## -syntax

````
typedef struct _AVC_STREAM_REQUEST_BLOCK {
  ULONG                 SizeOfThisBlock;
  ULONG                 Version;
  AVCSTRM_FUNCTION      Function;
  ULONG                 Flags;
  NTSTATUS              Status;
  PVOID                 AVCStreamContext;
  PVOID                 Context1;
  PVOID                 Context2;
  PVOID                 Context3;
  PVOID                 Context4;
  ULONG                 Reserved[4];
  union _tagCommandData  CommandData;
} AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field <b>SizeOfThisBlock</b>

<dd>
<p>Specifies the size of the request block in bytes. Do not set this value directly. Instead, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560750">INIT_AVCSTRM_HEADER</a> macro.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of <i>avcstrm.sys</i> device driver interface (DDI) to service a request. Do not set this value directly. Instead, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560750">INIT_AVCSTRM_HEADER</a> macro.</p>
</dd>

### -field <b>Function</b>

<dd>
<p>Indicates the request (function code) <i>avcstrm.sys</i> services. This must be a value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554120">AVCSTRM_FUNCTION</a> enumeration. Do not set this value directly. Instead, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560750">INIT_AVCSTRM_HEADER</a> macro.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Special flags to indicate special service or deviation from standard service. This is currently not used.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>Final status of this request.</p>
</dd>

### -field <b>AVCStreamContext</b>

<dd>
<p>This is context (handle) of a stream. Set this to <b>NULL</b> for the <b>AVCSTRM_OPEN</b> function code. For other function codes, this must be set to a valid value retrieved from an earlier call to AVCSTRM_OPEN.</p>
</dd>

### -field <b>Context1</b>

<dd>
<p>The context pointers of the client.</p>
</dd>

### -field <b>Context2</b>

<dd>
<p>The context pointers of the client.</p>
</dd>

### -field <b>Context3</b>

<dd>
<p>The context pointers of the client.</p>
</dd>

### -field <b>Context4</b>

<dd>
<p>The context pointers of the client.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>CommandData</b>

<dd>
<p>This is a union of command data to be passed to <i>avcstrm.sys</i> for service.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>StreamState</p>
</td>
<td>
<p>Specifies the current state of the specified stream. This is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554124">AVCSTRM_GET_STATE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554134">AVCSTRM_SET_STATE</a> function codes.</p>
</td>
</tr>
<tr>
<td>
<p>OpenStruct</p>
</td>
<td>
<p>Specifies a description of a stream to open. This is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554125">AVCSTRM_OPEN</a> function code.</p>
</td>
</tr>
<tr>
<td>
<p>BufferStruct</p>
</td>
<td>
<p>Specifies a description of a buffer used to read or write data from/to a specified stream. This is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554130">AVCSTRM_READ</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554135">AVCSTRM_WRITE</a> function codes.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The AVC_STREAM_REQUEST_BLOCK is the primary structure used by a subunit driver to interface with <i>avcstrm.sys</i>.</p>

<p>Every AV/C stream request is described by this structure. This structure is passed as part of the IRP to <i>avcstrm.sys</i> for service..</p>

<p>To use this structure, set the IRP's <b>Irp-&gt;Parameters-&gt;Others.Argument1</b> member to an allocated and initialized AVC_STREAM_REQUEST_BLOCK that describes the request (functionality) that the subunit driver wants <i>avcstrm.sys</i> to service.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Avcstrm.h (include Avcstrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554120">AVCSTRM_FUNCTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554127">AVCSTRM_OPEN_STRUCT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554108">AVCSTRM_BUFFER_STRUCT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554130">AVCSTRM_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554135">AVCSTRM_WRITE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554125">AVCSTRM_OPEN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554110">AVCSTRM_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554107">AVCSTRM_ABORT_STREAMING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554124">AVCSTRM_GET_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554134">AVCSTRM_SET_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554121">AVCSTRM_GET_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554132">AVCSTRM_SET_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVC_STREAM_REQUEST_BLOCK structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
