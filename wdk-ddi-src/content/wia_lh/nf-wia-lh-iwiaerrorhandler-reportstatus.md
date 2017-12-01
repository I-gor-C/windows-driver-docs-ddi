---
UID: NF.wia_lh.IWiaErrorHandler.ReportStatus
title: IWiaErrorHandler::ReportStatus
author: windows-driver-content
description: The IWiaErrorHandler::ReportStatus method displays information about an error or status during a transfer. In some cases this method allows the user to recover from an error.
old-location: image\iwiaerrorhandler_reportstatus.htm
old-project: image
ms.assetid: c244d5a1-d3c1-4f8f-9b55-3729e5f13887
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaErrorHandler, ReportStatus, IWiaErrorHandler::ReportStatus
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wia_lh.h
req.include-header: Wia.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaErrorHandler.ReportStatus
req.alt-loc: wia_lh.h
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
req.iface: IWiaErrorHandler
req.product: Windows 10 or later.
---

# IWiaErrorHandler::ReportStatus method



## -description
<p>The <b>IWiaErrorHandler::ReportStatus</b> method displays information about an error or status during a transfer. In some cases this method allows the user to recover from an error.</p>


## -syntax

````
HRESULT ReportStatus(
  [in] LONG      lFlags,
  [in] HWND      hwndParent,
  [in] IWiaItem2 *pWiaItem2,
  [in] HRESULT   hrStatus,
  [in] LONG      lPercentComplete
);
````


## -parameters
<dl>

### -param <i>lFlags</i> [in]

<dd>
<p>Currently unused. Should be set to zero. </p>
</dd>

### -param <i>hwndParent</i> [in]

<dd>
<p>Caller supplied handle of the window that should be used as the parent window for any dialog boxes. If this is set to <b>NULL</b>, no dialog boxes should be displayed.</p>
</dd>

### -param <i>pWiaItem2</i> [in]

<dd>
<p>Pointer to the <b>IWiaItem2</b> item being transferred. <b>IWiaItem2</b> is described in the Microsoft Windows SDK documentation.</p>
</dd>

### -param <i>hrStatus</i> [in]

<dd>
<p>HRESULT variable that contains the status code received by the WIA transfer method, for example the <b>IWiaDataCallback::BandedDataCallback</b> method (described in the Windows SDK documentation).</p>
</dd>

### -param <i>lPercentComplete</i> [in]

<dd>
<p>Size of the data, in bytes, the <i>pbData</i> pointer refers to.</p>
</dd>
</dl>

## -returns
<p>Returns a standard COM error code if the error cannot be recovered from, or if the user chooses to abort the transfer in response to the displayed dialog box. There is additional information on the return values in the remarks section. Otherwise this method returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Appropriate action was taken to correct the error and the transfer can continue.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>No action was taken to handle the error or report status to the user.</p>

<p> </p>

## -remarks
<p>The COM proxy callback object (described in the Windows SDK documentation) calls the <b>WiaErrorHandler::ReportStatus</b> method when the driver sends an IT_MSG_DEVICE_STATUS message to the <b>IWiaDataCallback::BandedDataCallback</b> method (described in the Windows SDK documentation). The dialog box that this method displays provides the user with error or status information and possibly gives an opportunity to recover from the error and continue the transfer. The UI should provide only an informational dialog box and a chance to cancel the transfer if the HRESULT is SEVERITY_SUCCESS.</p>

<p>A driver that implements this method, should display a modal dialog box, owned by <i>hwndParent</i>, in response to a value of <i>hrStatus</i> for which <b>FAILED</b>(<i>hrStatus</i>) evaluates to <b>TRUE</b>. If <b>FAILED</b>(<i>hrStatus</i>) evaluates to <b>FALSE</b>, the value in <i>hrStatus</i> represents a nonfatal delay, and the dialog box displayed should be modeless. The dialog box should be removed when the status of the transfer changes. An error handler should return S_FALSE for unknown values of <i>hrStatus</i>.</p>

<p>The <i>hrStatus</i> parameter is set to WIA_STATUS_TRANSFER_BEGIN to inform the handler that a transfer has started. It is set to WIA_STATUS_TRANSFER_END when the transfer is complete.</p>

<p>If <i>hrStatus</i> is S_OK, the data transfer has resumed and no delay or error is currently in effect.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.iwiaerrorhandler_getstatusdescription">IWiaErrorHandler::GetStatusDescription</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaErrorHandler::ReportStatus method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
