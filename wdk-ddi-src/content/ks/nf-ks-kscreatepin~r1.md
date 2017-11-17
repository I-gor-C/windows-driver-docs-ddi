---
UID: NF.ks.KsCreatePin~r1
title: KsCreatePin
author: windows-driver-content
description: The KsCreatePin function passes a connection request to a device, creating a pin instance. This function can only be called at PASSIVE_LEVEL for kernel-mode clients.
old-location: stream\kscreatepin.htm
ms.assetid: 0dae335a-bcc1-4f6a-8926-e2ecc4112dc5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCreatePin
req.alt-loc: ks.lib,ks.dll,ksuser.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsCreatePin
req.iface: 
---

# KsCreatePin function



## -description
<p>The <b>KsCreatePin</b> function passes a connection request to a device, creating a pin instance. This function can only be called at <b>PASSIVE_LEVEL</b> for kernel-mode clients.</p>


## -syntax

````
NTSTATUS KsCreatePin(
  _In_  HANDLE         FilterHandle,
  _In_  PKSPIN_CONNECT Connect,
  _In_  ACCESS_MASK    DesiredAccess,
  _Out_ PHANDLE        ConnectionHandle
);
````


## -parameters
<dl>

### -param <i>FilterHandle</i> [in]

<dd>
<p>Specifies the handle of the filter initiating the create request and where the connection will occur. </p>
</dd>

### -param <i>Connect</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563531">KSPIN_CONNECT</a> structure that contains parameters for the requested connection. This should be followed in memory by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a> data structure, describing the data format requested for the connection.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies the access desired to the pin. This is typically <b>GENERIC_READ</b> or <b>GENERIC_WRITE</b>. For data flowing into the pin this value should be set to <b>GENERIC_WRITE</b>, and for data flowing out of the pin this should be set to <b>GENERIC_READ</b> regardless of the communication method.</p>
</dd>

### -param <i>ConnectionHandle</i> [out]

<dd>
<p>Specifies the connection handle passed. The routine fills this in with a handle to the file object of the created connection. This value can then be used to disconnect with the <a href="base.closehandle">CloseHandle</a> function.</p>
</dd>
</dl>

## -returns
<p>The <b>KsCreatePin</b> function returns <b>STATUS_SUCCESS</b> if the connection was successful, or it returns an error if the connection failed. Additionally, this Win32 error code (from Winerror.h) can be returned:</p><dl>
<dt><b>ERROR_NO_MATCH</b></dt>
<dd>
<p>1169L (0x491)</p>
<p>The connection failed because the interface, medium, or data format were not found.</p>
<div class="alert"><b>Note</b>  Do not rely on using the <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>  macro to check return codes from this function: the  macro could evaluate to <b>TRUE</b> even though the function returns the <b>ERROR_NO_MATCH</b> error code.</div>
<div> </div>
</dd>
</dl><p>1169L (0x491)</p>

<p>The connection failed because the interface, medium, or data format were not found.</p>

## -remarks
<p>The routine sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request to the driver. The driver accepts the request only if the interface, medium, and data format are compatible.</p>

<p>If <i>Connect</i>-&gt;<b>PinToHandle</b> is <b>NULL</b>, <b>KsCreatePin</b> creates a pin the caller can use to send requests to the streaming driver specified in <i>Connect</i>-&gt;<b>FilterHandle</b>. <i>Connect</i>-&gt;<b>PinId</b> determines the pin type of the pin to be created.</p>

<p>The routine sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request to the driver. The driver accepts the request only if the interface, medium, and data format are compatible.</p>

<p>If <i>Connect</i>-&gt;<b>PinToHandle</b> is <b>NULL</b>, <b>KsCreatePin</b> creates a pin the caller can use to send requests to the streaming driver specified in <i>Connect</i>-&gt;<b>FilterHandle</b>. <i>Connect</i>-&gt;<b>PinId</b> determines the pin type of the pin to be created.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563531">KSPIN_CONNECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsCreatePin function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
