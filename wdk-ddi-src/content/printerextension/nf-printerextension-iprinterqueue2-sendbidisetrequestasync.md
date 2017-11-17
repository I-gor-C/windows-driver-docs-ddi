---
UID: NF.printerextension.IPrinterQueue2.SendBidiSetRequestAsync
title: IPrinterQueue2::SendBidiSetRequestAsync
author: windows-driver-content
description: Uses an XML string value to send a Bidi Set request as an asynchronous operation.
old-location: print\iprinterqueue2_sendbidisetrequestasync.htm
ms.assetid: 05FF8A47-A586-4DA7-94AD-A7186265ADB4
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueue2.SendBidiSetRequestAsync
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: IPrinterQueue2, SendBidiSetRequestAsync, IPrinterQueue2::SendBidiSetRequestAsync
req.iface: IPrinterQueue2
req.product: Windows 10 or later.
---

# IPrinterQueue2::SendBidiSetRequestAsync method



## -description
<p>Uses an XML string value to send a Bidi Set request as an asynchronous operation.</p>
<p>This method allows the user to perform device maintenance tasks from within a UWP device app  for printers.</p>


## -syntax

````
HRESULT SendBidiSetRequestAsync(
  [in]          BSTR                            bstrBidiRequest,
  [in]          IPrinterBidiSetRequestCallback  *pCallback,
  [out, retval] IPrinterExtensionAsyncOperation ** ppAsyncOperation
);
````


## -parameters
<dl>

### -param <i>bstrBidiRequest</i> [in]

<dd>
<p>XML string that is used to transfer the data for the  Set request.</p>
</dd>

### -param <i>pCallback</i> [in]

<dd>
<p>Callback object for the Bidi Set request.</p>
</dd>

### -param <i> ppAsyncOperation</i> [out, retval]

<dd>
<p>Context object associated with the asynchronous Bidi Set  request (operation).</p>
</dd>
</dl>

## -returns
<p>This method returns the appropriate <b>HRESULT</b> value.</p>

## -remarks


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
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265385">IPrinterBidiSetRequestCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265387">IPrinterExtensionAsyncOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265389">IPrinterQueue2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueue2::SendBidiSetRequestAsync method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
