---
UID: NF.wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoInit
title: IPnpCallbackSelfManagedIo::OnSelfManagedIoInit
author: windows-driver-content
description: The OnSelfManagedIoInit method initializes a device's self-managed I/O operations.
old-location: wdf\ipnpcallbackselfmanagedio_onselfmanagedioinit.htm
old-project: wdf
ms.assetid: 41b12fef-dbc7-4b91-a2d3-9fb1aafff237
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IPnpCallbackSelfManagedIo, OnSelfManagedIoInit, IPnpCallbackSelfManagedIo::OnSelfManagedIoInit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPnpCallbackSelfManagedIo.OnSelfManagedIoInit
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IPnpCallbackSelfManagedIo
req.product: Windows 10 or later.
---

# IPnpCallbackSelfManagedIo::OnSelfManagedIoInit method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnSelfManagedIoInit</b> method initializes a device's self-managed I/O operations.</p>


## -syntax

````
HRESULT OnSelfManagedIoInit(
  [in] IWDFDevice *pWdfDevice
);
````


## -parameters
<dl>

### -param pWdfDevice [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a> interface for the device object of the device for which the self-managed I/O operations are initialized.</p>
</dd>
</dl>

## -returns
<p>If the <b>OnSelfManagedIoInit</b> callback encounters no errors, it must return
        S_OK or another status code for which SUCCEEDED(status) equals <b>TRUE</b>.</p>

<p>  If it returns a status code for which SUCCEEDED(status) equals <b>FALSE</b>, the framework will not start the device. In this case, the framework calls the driver's <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioflush">IPnpCallbackSelfManagedIo::OnSelfManagedIoFlush</a> and <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediocleanup">IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup</a> callback methods.</p>

<p>HRESULT error codes are defined in Winerror.h. </p>

## -remarks
<p>A driver registers the <a href="..\wudfddi\nn-wudfddi-ipnpcallbackselfmanagedio.md">IPnpCallbackSelfManagedIo</a> interface when it calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-ipnpcallbackselfmanagedio.md">IPnpCallbackSelfManagedIo</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackSelfManagedIo::OnSelfManagedIoInit method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
