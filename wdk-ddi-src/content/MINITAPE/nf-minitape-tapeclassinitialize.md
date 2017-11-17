---
UID: NF.minitape.TapeClassInitialize
title: TapeClassInitialize
author: windows-driver-content
description: The TapeClassInitialize routine performs much of the driver and device initialization on behalf of a miniclass driver.
old-location: storage\tapeclassinitialize.htm
ms.assetid: f1c70ca5-2caf-4758-99bb-221af0a79211
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeClassInitialize
req.alt-loc: Tape.lib,Tape.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Tape.lib
req.dll: 
req.irql: 
ms.keywords: TapeClassInitialize
req.iface: 
---

# TapeClassInitialize function



## -description
<p>The <b>TapeClassInitialize</b> routine performs much of the driver and device initialization on behalf of a miniclass driver. <b>TapeClassInitialize</b> loads the tape class driver entry points for tape I/O requests into the miniclass driver data structure, locates and claims unclaimed tape devices that the miniclass driver supports, and allocates and initializes the operating system resources for the miniclass driver and its devices. <b>TapeClassInitialize</b> uses miniclass-driver-specific information supplied in <i>TapeInitData</i> and calls back to the tape miniclass driver for driver-specific operations.</p>


## -syntax

````
ULONG TapeClassInitialize(
  _In_ PVOID              Argument1,
  _In_ PVOID              Argument2,
  _In_ PTAPE_INIT_DATA_EX TapeInitData
);
````


## -parameters
<dl>

### -param <i>Argument1</i> [in]

<dd>
<p>Pointer to driver context information that was passed to the tape miniclass driver's <b>DriverEntry</b> routine. The format of the information is operating system-specific and must not be interpreted by a tape miniclass driver.</p>
</dd>

### -param <i>Argument2</i> [in]

<dd>
<p>Pointer to the second driver context structure that was passed to the tape miniclass driver's<b> DriverEntry</b> routine. The format of the information is operating system-specific and must not be interpreted by a tape miniclass driver.</p>
</dd>

### -param <i>TapeInitData</i> [in]

<dd>
<p>Pointer to a TAPE_INIT_DATA_EX structure containing driver-specific information such as the entry points for the tape miniclass driver's command processing routines.</p>
</dd>
</dl>

## -returns
<p><b>TapeClassInitialize</b> returns a value indicating the success or failure of the driver initialization. The tape miniclass driver passes this value, uninterpreted, as the return value from its <b>DriverEntry</b> routine.</p>

## -remarks
<p>A tape miniclass driver calls <b>TapeClassInitialize</b> from its <b>DriverEntry</b> routine and passes driver-specific information in <i>TapeInitData</i>. <b>TapeClassInitialize</b> performs a large part of the driver initialization on behalf of the miniclass driver and insulates the miniclass driver from operating system-specific details.</p>

<p><b>TapeClassInitialize</b> calls the tape miniclass driver for driver-specific activities required during initialization. For example, <b>TapeClassInitialize</b> calls the tape miniclass driver's TapeMiniVerifyInquiry routine to determine whether the driver supports a given tape device. <b>TapeClassInitialize</b> also calls the tape miniclass driver's TapeMiniExtensionInit routine to initialize the minitape extension, if the miniclass driver requested one.</p>

<p>A tape miniclass driver allocates a TAPE_INIT_DATA_EX structure on the stack, clears it with <b>TapeClassZeroMemory</b>, fills in all the appropriate members, and passes it to <b>TapeClassInitialize</b>.</p>

<p>A tape miniclass driver calls <b>TapeClassInitialize</b> from its <b>DriverEntry</b> routine and passes driver-specific information in <i>TapeInitData</i>. <b>TapeClassInitialize</b> performs a large part of the driver initialization on behalf of the miniclass driver and insulates the miniclass driver from operating system-specific details.</p>

<p><b>TapeClassInitialize</b> calls the tape miniclass driver for driver-specific activities required during initialization. For example, <b>TapeClassInitialize</b> calls the tape miniclass driver's TapeMiniVerifyInquiry routine to determine whether the driver supports a given tape device. <b>TapeClassInitialize</b> also calls the tape miniclass driver's TapeMiniExtensionInit routine to initialize the minitape extension, if the miniclass driver requested one.</p>

<p>A tape miniclass driver allocates a TAPE_INIT_DATA_EX structure on the stack, clears it with <b>TapeClassZeroMemory</b>, fills in all the appropriate members, and passes it to <b>TapeClassInitialize</b>.</p>

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
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Tape.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567968">TAPE_INIT_DATA_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552656">DriverEntry of Tape Miniclass Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20TapeClassInitialize routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
