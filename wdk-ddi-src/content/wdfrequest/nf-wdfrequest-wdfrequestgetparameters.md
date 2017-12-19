---
UID: NF.wdfrequest.WdfRequestGetParameters
title: WdfRequestGetParameters function
author: windows-driver-content
description: The WdfRequestGetParameters method retrieves the parameters that are associated with a specified framework request object.
old-location: wdf\wdfrequestgetparameters.htm
old-project: wdf
ms.assetid: 7d9924a9-23b6-4bec-95f0-cebc3e99fda4
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestGetParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestGetParameters
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, evtioresumegetparam, evtiostopgetparam, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfRequestGetParameters function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestGetParameters</b> method retrieves the parameters that are associated with a specified framework request object.



## -syntax

````
VOID WdfRequestGetParameters(
  _In_  WDFREQUEST              Request,
  _Out_ PWDF_REQUEST_PARAMETERS Parameters
);
````


## -parameters

### -param Request [in]

A handle to a framework request object. 


### -param Parameters [out]

A pointer to a caller-allocated <a href="wdf.wdf_request_parameters">WDF_REQUEST_PARAMETERS</a> structure that the <a href="wdf.wdf_request_parameters_init">WDF_REQUEST_PARAMETERS_INIT</a> routine initialized and filled in.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
A driver cannot retrieve parameters from a driver-created request by calling <b>WdfRequestGetParameters</b>  because the framework does not allocate a stack location for the current driver.

For more information about <b>WdfRequestGetParameters</b>, see <a href="wdf.obtaining_information_about_an_i_o_request">Obtaining Information About an I/O Request</a>.

For a code example that uses <b>WdfRequestGetParameters</b>, see <a href="wdf.wdfrequestcomplete">WdfRequestComplete</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_evtioresumegetparam">evtioresumegetparam</a>, <a href="devtest.kmdf_evtiostopgetparam">evtiostopgetparam</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestwdmgetirp">WdfRequestWdmGetIrp</a>
</dt>
<dt>
<a href="wdf.wdf_request_parameters_init">WDF_REQUEST_PARAMETERS_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_request_parameters">WDF_REQUEST_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetParameters method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

