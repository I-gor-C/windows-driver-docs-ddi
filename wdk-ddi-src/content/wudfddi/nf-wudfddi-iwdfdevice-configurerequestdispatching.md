---
UID: NF.wudfddi.IWDFDevice.ConfigureRequestDispatching
title: IWDFDevice::ConfigureRequestDispatching method
author: windows-driver-content
description: The ConfigureRequestDispatching method configures the queuing of I/O requests of the specified type to the specified I/O queue.
old-location: wdf\iwdfdevice_configurerequestdispatching.htm
old-project: wdf
ms.assetid: b3318695-e9f2-480a-9133-9008ef0002b7
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFDevice, IWDFDevice::ConfigureRequestDispatching, ConfigureRequestDispatching
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.ConfigureRequestDispatching
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFDevice::ConfigureRequestDispatching method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>ConfigureRequestDispatching</b> method configures the queuing of I/O requests of the specified type to the specified I/O queue.



## -syntax

````
HRESULT ConfigureRequestDispatching(
  [in] IWDFIoQueue      *pQueue,
  [in] WDF_REQUEST_TYPE RequestType,
  [in] BOOL             Forward
);
````


## -parameters

### -param pQueue [in]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfioqueue.md">IWDFIoQueue</a> interface for the I/O queue to configure. 


### -param RequestType [in]

A <a href="wdf.wdf_request_type__umdf_">WDF_REQUEST_TYPE</a>-typed value that identifies the request type to be queued. The only valid <b>WDF_REQUEST_TYPE</b> values are <b>WdfRequestCreate</b>, <b>WdfRequestRead</b>, <b>WdfRequestWrite</b>, and <b>WdfRequestDeviceIoControl</b>.


### -param Forward [in]

A BOOL value that specifies whether requests of the specified type are queued. <b>TRUE</b> indicates to enable queuing requests; <b>FALSE</b> indicates to disable queuing requests.


## -returns
<b>ConfigureRequestDispatching</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.

The following code example shows how to configure a queue.


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
1.5

</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfioqueue.md">IWDFIoQueue</a>
</dt>
<dt>
<a href="wdf.wdf_request_type__umdf_">WDF_REQUEST_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::ConfigureRequestDispatching method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

