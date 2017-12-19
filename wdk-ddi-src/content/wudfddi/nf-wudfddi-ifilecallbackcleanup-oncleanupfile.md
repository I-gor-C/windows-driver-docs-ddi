---
UID: NF.wudfddi.IFileCallbackCleanup.OnCleanupFile
title: IFileCallbackCleanup::OnCleanupFile method
author: windows-driver-content
description: The OnCleanupFile method cancels all I/O requests that a driver has pending in the framework queue.
old-location: wdf\ifilecallbackcleanup_oncleanupfile.htm
old-project: wdf
ms.assetid: e6dd18f4-725f-4611-ad70-029654cf4375
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IFileCallbackCleanup, IFileCallbackCleanup::OnCleanupFile, OnCleanupFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IFileCallbackCleanup.OnCleanupFile
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
req.irql: 
req.product: Windows 10 or later.
---

# IFileCallbackCleanup::OnCleanupFile method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>OnCleanupFile</b> method cancels all I/O requests that a driver has pending in the framework queue. 



## -syntax

````
void OnCleanupFile(
  [in] IWDFFile *pWdfFileObject
);
````


## -parameters

### -param pWdfFileObject [in]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface for the file object that is associated with the device. 


## -returns
None


## -remarks
A driver registers the <a href="..\wudfddi\nn-wudfddi-ifilecallbackcleanup.md">IFileCallbackCleanup</a> interface when the driver calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. 

The framework calls the <b>OnCleanupFile</b> method to notify the driver to cancel all I/O requests that it has pending. The framework notifies the driver in response to an application calling the Microsoft Win32 <b>CloseHandle</b> function. 

For information about when the framework calls <b>OnCleanupFile</b>, see <a href="wdf.driver_created_versus_application_created_file_objects">Driver-Created Versus Application-Created File Objects</a>.


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\wudfddi\nn-wudfddi-ifilecallbackcleanup.md">IFileCallbackCleanup</a>
</dt>
<dt>
<a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IFileCallbackCleanup::OnCleanupFile method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

