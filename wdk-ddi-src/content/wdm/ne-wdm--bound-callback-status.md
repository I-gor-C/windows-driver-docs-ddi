---
UID: NE.wdm._BOUND_CALLBACK_STATUS
title: BOUND_CALLBACK_STATUS
author: windows-driver-content
description: The BOUND_CALLBACK_STATUS enumeration indicates how a user-mode bounds exception was processed by the BoundCallback function.
old-location: kernel\bound_callback_status.htm
old-project: kernel
ms.assetid: 874FB2E1-7A2F-4C91-BA72-D67DA2EE84E1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BOUND_CALLBACK_STATUS
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# BOUND_CALLBACK_STATUS enumeration



## -description
<p>The <b>BOUND_CALLBACK_STATUS</b> enumeration indicates how a user-mode bounds exception was processed by the <a href="kernel.boundcallback">BoundCallback</a> function.</p>


## -syntax

````
typedef enum _BOUND_CALLBACK_STATUS { 
  BoundExceptionContinueSearch  = 0,
  BoundExceptionHandled,
  BoundExceptionError,
  BoundExceptionMaximum
} BOUND_CALLBACK_STATUS;
````


## -enum-fields
<dl>

### -field <a id="BoundExceptionContinueSearch"></a><a id="boundexceptioncontinuesearch"></a><a id="BOUNDEXCEPTIONCONTINUESEARCH"></a><b>BoundExceptionContinueSearch</b>

<dd>
<p>The bounds exception was not handled by the callback, and the exception should continue to propagate.  </p>
</dd>

### -field <a id="BoundExceptionHandled"></a><a id="boundexceptionhandled"></a><a id="BOUNDEXCEPTIONHANDLED"></a><b>BoundExceptionHandled</b>

<dd>
<p>The exception was handled by the callback, and the exception should not propagate any further. </p>
</dd>

### -field <a id="BoundExceptionError"></a><a id="boundexceptionerror"></a><a id="BOUNDEXCEPTIONERROR"></a><b>BoundExceptionError</b>

<dd>
<p>The user mode process should be terminated by the system.</p>
</dd>

### -field <a id="BoundExceptionMaximum"></a><a id="boundexceptionmaximum"></a><a id="BOUNDEXCEPTIONMAXIMUM"></a><b>BoundExceptionMaximum</b>

<dd>
<p>This value is not currently used.</p>
</dd>
</dl>

## -remarks
<p>The return value of the <a href="kernel.boundcallback">BoundCallback</a> routine is a <b>BOUND_CALLBACK_STATUS</b> value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.boundcallback">BoundCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BOUND_CALLBACK_STATUS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
