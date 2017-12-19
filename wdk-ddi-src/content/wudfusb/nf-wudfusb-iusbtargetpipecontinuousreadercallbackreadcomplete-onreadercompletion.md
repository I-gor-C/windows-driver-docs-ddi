---
UID: NF.wudfusb.IUsbTargetPipeContinuousReaderCallbackReadComplete.OnReaderCompletion
title: IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion method
author: windows-driver-content
description: A driver's OnReaderCompletion event callback function informs the driver that a continuous reader has successfully completed a read request.
old-location: wdf\iusbtargetpipecontinuousreadercallbackreadcomplete_onreadercompletion.htm
old-project: wdf
ms.assetid: 946e0206-7609-4dc7-91c2-a6aadad91751
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IUsbTargetPipeContinuousReaderCallbackReadComplete, IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion, OnReaderCompletion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IUsbTargetPipeContinuousReaderCallbackReadComplete.OnReaderCompletion
req.alt-loc: wudfusb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver's <b>OnReaderCompletion</b> event callback function informs the driver that a continuous reader has successfully completed a read request.



## -syntax

````
void OnReaderCompletion(
  [in] IWDFUsbTargetPipe *pPipe,
  [in] IWDFMemory        *pMemory,
  [in] SIZE_T            NumBytesTransferred,
  [in] PVOID             Context
);
````


## -parameters

### -param pPipe [in]

A pointer to the <a href="..\wudfusb\nn-wudfusb-iwdfusbtargetpipe.md">IWDFUsbTargetPipe</a> interface for the USB pipe on which the driver has enabled a continuous reader.


### -param pMemory [in]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface for a read buffer that contains data that was read from the USB pipe.


### -param NumBytesTransferred [in]

The number of bytes that the read buffer contains.


### -param Context [in]

A pointer to driver-supplied context information that the driver provided when it previously called <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a>.


## -returns
None.


## -remarks
To register an <b>IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion</b> callback function, your driver must provide a pointer to the driver's <a href="..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete.md">IUsbTargetPipeContinuousReaderCallbackReadComplete</a> interface when it calls <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a>.

If a driver has created a continuous reader for a USB pipe, the framework calls the driver's <b>OnReaderCompletion</b> callback function each time the driver's I/O target successfully completes a read request. If the I/O target does not successfully complete a request, the framework calls the driver's <a href="wdf.iusbtargetpipecontinuousreadercallbackreadersfailed_onreaderfailure">IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure</a> callback function. 

To access the buffer that contains data that was read from the device, the driver can call <a href="wdf.iwdfmemory_getdatabuffer">IWDFMemory::GetDataBuffer</a>. The framework writes the data into the buffer, after the header that is defined by the <i>HeaderLength</i> parameter of <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a>. Note that the pointer that <b>IWDFMemory::GetDataBuffer</b> returns points to the beginning of the header, but the <b>OnReaderCompletion</b> callback function's <i>NumBytesTransferred</i> parameter does not include the header's length.

By default, the framework deletes the buffer's memory object after the <b>OnReaderCompletion</b> callback function returns. However, you might want the memory object to remain valid after the callback function returns. For example, you might want your driver to store the memory object's interface pointer in the framework pipe object's <a href="wdf.iwdfobject_assigncontext">context space</a> so that the driver can process the memory object's contents after the callback function returns. To extend the lifetime of the memory object, the callback function must call the buffer's <a href="wdf.umdf_based_on_com_subset">IWDFMemory::AddRef</a> method. Subsequently, the driver must call the buffer's <a href="wdf.umdf_based_on_com_subset">IWDFMemory::Release</a> method so that the framework can delete the object.

The framework synchronizes calls to the <b>OnReaderCompletion</b> and <a href="wdf.iusbtargetpipecontinuousreadercallbackreadersfailed_onreaderfailure">IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure</a> callback functions according to the following rules:

These callback functions do not run simultaneously for an individual USB pipe.

If the driver creates multiple continuous readers for multiple USB pipes, with multiple <b>OnReaderCompletion</b> and <a href="wdf.iusbtargetpipecontinuousreadercallbackreadersfailed_onreaderfailure">OnReaderFailure</a> callback functions, the multiple callback functions can run simultaneously.

If the driver has specified the default <i>NumPendingReads</i> value when it calls <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> (or if it specifies any <i>NumPendingReads</i> value that is greater than 1), and if a read request completes while the <b>OnReaderCompletion</b> callback function is executing, the framework can call the <b>OnReaderCompletion</b> callback function again before the callback function returns.

The framework does not synchronize these callback functions with any other callback functions.

When your driver calls <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a>, it can specify an <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> callback function. The framework will call that callback function when it attempts to delete the memory object, after the <b>OnReaderCompletion</b> callback function returns. 

For more information about the <b>OnReaderCompletion</b> callback function and USB I/O targets, see <a href="wdf.usb_i_o_targets_in_umdf">Handling a USB I/O Target</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfusb.h (include Wudfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete.md">IUsbTargetPipeContinuousReaderCallbackReadComplete</a>
</dt>
<dt>
<a href="wdf.iusbtargetpipecontinuousreadercallbackreadersfailed_onreaderfailure">IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

