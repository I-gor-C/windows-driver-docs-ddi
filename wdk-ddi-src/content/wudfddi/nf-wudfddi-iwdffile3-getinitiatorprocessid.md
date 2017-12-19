---
UID: NF.wudfddi.IWDFFile3.GetInitiatorProcessId
title: IWDFFile3::GetInitiatorProcessId method
author: windows-driver-content
description: The GetInitiatorProcessId method retrieves the initiator process ID associated with an IWDFFile interface.
old-location: wdf\iwdffile3_getinitiatorprocessid.htm
old-project: wdf
ms.assetid: 4D23A651-7231-40CE-B9C2-4382D4E7F683
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFFile3, IWDFFile3::GetInitiatorProcessId, GetInitiatorProcessId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFFile3.GetInitiatorProcessId
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

# IWDFFile3::GetInitiatorProcessId method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>GetInitiatorProcessId</b> method retrieves the initiator process ID associated with an <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface.



## -syntax

````
void GetInitiatorProcessId(
  [out] DWORD *pdwProcessId
);
````


## -parameters

### -param pdwProcessId [out]

Specifies the address of a location that receives the initiator process identifier associated with the file, if any exists.  Otherwise, the location receives 0.


## -returns
This method does not return a value.


## -remarks
Starting in Windows 8, a system component may issue a create on behalf of an app. The driver can call <b>GetInitiatorProcessId</b> to determine which process the create operation is ultimately intended for.

<b>GetInitiatorProcessId</b> returns zero if no initiator process is associated with the create operation.

For more information about framework file objects, see <a href="wdf.driver_created_versus_application_created_file_objects">Driver-Created Versus Application-Created File Objects</a>.


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
1.11

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
<a href="..\wudfddi\nn-wudfddi-iwdffile3.md">IWDFFile3</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFFile3::GetInitiatorProcessId method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

