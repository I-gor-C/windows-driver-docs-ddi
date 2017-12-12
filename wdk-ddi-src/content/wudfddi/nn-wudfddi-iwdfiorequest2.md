---
UID: NN.wudfddi.IWDFIoRequest2
title: IWDFIoRequest2
author: windows-driver-content
description: To obtain the IWDFIoRequest2 interface, drivers call IWDFIoRequest::QueryInterface.
old-location: wdf\iwdfiorequest2.htm
old-project: wdf
ms.assetid: 6a6285c9-8366-4487-a1c5-38aa24d172a9
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFIoRequest2
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# IWDFIoRequest2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFIoRequest2</b> interface, drivers call <b>IWDFIoRequest::QueryInterface</b>.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoRequest2</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a>. <b>IWDFIoRequest2</b> also has these types of members:

The <b>IWDFIoRequest2</b> interface has these methods.

The <a href="wdf.iwdfiorequest2_getcreateparametersex">GetCreateParametersEx</a> method retrieves file creation parameters that are associated with a file that is being created or opened.

The <a href="wdf.iwdfiorequest2_geteffectiveiotype">GetEffectiveIoType</a> method returns the buffer access method that UMDF is using for the data buffers of the I/O request that the <b>IWDFIoRequest2</b> interface represents.

The <a href="wdf.iwdfiorequest2_getqueryinformationparameters">GetQueryInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestQueryInformation</a>-typed I/O request.

The <a href="wdf.iwdfiorequest2_getrequestormode">GetRequestorMode</a> method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver).

The <a href="wdf.iwdfiorequest2_getsetinformationparameters">GetSetInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestSetInformation</a>-typed I/O request.

The <a href="wdf.iwdfiorequest2_getstatus">GetStatus</a> method returns the status of an I/O request.

The <a href="wdf.iwdfiorequest2_iscanceled">IsCanceled</a> method determines whether the I/O manager has attempted to cancel an I/O request.

The <a href="wdf.iwdfiorequest2_isfromusermodedriver">IsFromUserModeDriver</a> method indicates whether an I/O request came from a user-mode driver or an application.

The <a href="wdf.iwdfiorequest2_requeue">Requeue</a> method returns an I/O request to the head of the I/O queue from which it was delivered to the driver.

The <a href="wdf.wdfrequestretrieveinputbuffer">RequestRetrieveInputBuffer</a> method retrieves an I/O request's input buffer.

The <a href="wdf.iwdfiorequest2_retrieveinputmemory">RetrieveInputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's input buffer.

The <a href="wdf.wdfrequestretrieveoutputbuffer">RequestRetrieveOutputBuffer</a> method retrieves an I/O request's output buffer.

The <a href="wdf.iwdfiorequest2_retrieveoutputmemory">RetrieveOutputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's output buffer.

The <a href="wdf.iwdfiorequest2_reuse">Reuse</a> method reinitializes a framework request object so that it can be reused.

The <a href="wdf.iwdfiorequest2_stopacknowledge">StopAcknowledge</a> method informs the framework that the driver has stopped processing a specified I/O request.

 


## -members
The <b>IWDFIoRequest2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_getcreateparametersex">IWDFIoRequest2::GetCreateParametersEx</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_getcreateparametersex">GetCreateParametersEx</a> method retrieves file creation parameters that are associated with a file that is being created or opened.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_geteffectiveiotype">IWDFIoRequest2::GetEffectiveIoType</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_geteffectiveiotype">GetEffectiveIoType</a> method returns the buffer access method that UMDF is using for the data buffers of the I/O request that the <b>IWDFIoRequest2</b> interface represents.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_getqueryinformationparameters">IWDFIoRequest2::GetQueryInformationParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_getqueryinformationparameters">GetQueryInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestQueryInformation</a>-typed I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_getrequestormode">IWDFIoRequest2::GetRequestorMode</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_getrequestormode">GetRequestorMode</a> method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver).

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_getsetinformationparameters">IWDFIoRequest2::GetSetInformationParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_getsetinformationparameters">GetSetInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestSetInformation</a>-typed I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_getstatus">IWDFIoRequest2::GetStatus</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_getstatus">GetStatus</a> method returns the status of an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_iscanceled">IWDFIoRequest2::IsCanceled</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_iscanceled">IsCanceled</a> method determines whether the I/O manager has attempted to cancel an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_isfromusermodedriver">IWDFIoRequest2::IsFromUserModeDriver</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_isfromusermodedriver">IsFromUserModeDriver</a> method indicates whether an I/O request came from a user-mode driver or an application.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_requeue">IWDFIoRequest2::Requeue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_requeue">Requeue</a> method returns an I/O request to the head of the I/O queue from which it was delivered to the driver.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_retrieveinputbuffer">IWDFIoRequest2::RetrieveInputBuffer</a>
</td>
<td align="left" width="63%">
The <a href="wdf.wdfrequestretrieveinputbuffer">RequestRetrieveInputBuffer</a> method retrieves an I/O request's input buffer.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_retrieveinputmemory">IWDFIoRequest2::RetrieveInputMemory</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_retrieveinputmemory">RetrieveInputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's input buffer.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_retrieveoutputbuffer">IWDFIoRequest2::RetrieveOutputBuffer</a>
</td>
<td align="left" width="63%">
The <a href="wdf.wdfrequestretrieveoutputbuffer">RequestRetrieveOutputBuffer</a> method retrieves an I/O request's output buffer.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_retrieveoutputmemory">IWDFIoRequest2::RetrieveOutputMemory</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_retrieveoutputmemory">RetrieveOutputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's output buffer.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_reuse">IWDFIoRequest2::Reuse</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_reuse">Reuse</a> method reinitializes a framework request object so that it can be reused.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest2_stopacknowledge">IWDFIoRequest2::StopAcknowledge</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest2_stopacknowledge">StopAcknowledge</a> method informs the framework that the driver has stopped processing a specified I/O request.

</td>
</tr>
</table>The <a href="wdf.iwdfiorequest2_getcreateparametersex">GetCreateParametersEx</a> method retrieves file creation parameters that are associated with a file that is being created or opened.

The <a href="wdf.iwdfiorequest2_geteffectiveiotype">GetEffectiveIoType</a> method returns the buffer access method that UMDF is using for the data buffers of the I/O request that the <b>IWDFIoRequest2</b> interface represents.

The <a href="wdf.iwdfiorequest2_getqueryinformationparameters">GetQueryInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestQueryInformation</a>-typed I/O request.

The <a href="wdf.iwdfiorequest2_getrequestormode">GetRequestorMode</a> method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver).

The <a href="wdf.iwdfiorequest2_getsetinformationparameters">GetSetInformationParameters</a> method retrieves parameters that are associated with a <a href="wdf.wdf_request_type__umdf_">WdfRequestSetInformation</a>-typed I/O request.

The <a href="wdf.iwdfiorequest2_getstatus">GetStatus</a> method returns the status of an I/O request.

The <a href="wdf.iwdfiorequest2_iscanceled">IsCanceled</a> method determines whether the I/O manager has attempted to cancel an I/O request.

The <a href="wdf.iwdfiorequest2_isfromusermodedriver">IsFromUserModeDriver</a> method indicates whether an I/O request came from a user-mode driver or an application.

The <a href="wdf.iwdfiorequest2_requeue">Requeue</a> method returns an I/O request to the head of the I/O queue from which it was delivered to the driver.

The <a href="wdf.wdfrequestretrieveinputbuffer">RequestRetrieveInputBuffer</a> method retrieves an I/O request's input buffer.

The <a href="wdf.iwdfiorequest2_retrieveinputmemory">RetrieveInputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's input buffer.

The <a href="wdf.wdfrequestretrieveoutputbuffer">RequestRetrieveOutputBuffer</a> method retrieves an I/O request's output buffer.

The <a href="wdf.iwdfiorequest2_retrieveoutputmemory">RetrieveOutputMemory</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface of a framework memory object that represents an I/O request's output buffer.

The <a href="wdf.iwdfiorequest2_reuse">Reuse</a> method reinitializes a framework request object so that it can be reused.

The <a href="wdf.iwdfiorequest2_stopacknowledge">StopAcknowledge</a> method informs the framework that the driver has stopped processing a specified I/O request.

 


## -remarks


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
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>