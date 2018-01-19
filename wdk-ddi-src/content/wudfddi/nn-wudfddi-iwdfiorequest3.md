---
UID : NN:wudfddi.IWDFIoRequest3
title : IWDFIoRequest3
author : windows-driver-content
description : To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest::QueryInterface.
old-location : wdf\iwdfiorequest3.htm
old-project : wdf
ms.assetid : 12F4CDB7-EEA5-49D1-AD41-6F5F0C9ED6C3
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : IWDFWorkItem, IWDFWorkItem::GetParentObject, GetParentObject
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.11
req.alt-api : IWDFIoRequest3
req.alt-loc : WUDFx.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : WUDFx.dll
req.irql : 
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IWDFIoRequest3 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFIoRequest3</b> interface, drivers call <b>IWDFIoRequest::QueryInterface</b>.

## Methods

<p>The <b>IWDFIoRequest3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFIoRequest3.GetUserModeDriverInitiatedIo](nf-wudfddi-iwdfiorequest3-getusermodedriverinitiatedio.md) | The GetUserModeDriverInitiatedIo method determines whether an I/O request is marked as initiated by a UMDF driver. |
| [wudfddi.IWDFIoRequest3.RetrieveActivityId](nf-wudfddi-iwdfiorequest3-retrieveactivityid.md) | The RetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [wudfddi.IWDFIoRequest3.SetActivityId](nf-wudfddi-iwdfiorequest3-setactivityid.md) | The SetActivityId method associates an activity identifier with an I/O request. |
| [wudfddi.IWDFIoRequest3.SetUserModeDriverInitiatedIo](nf-wudfddi-iwdfiorequest3-setusermodedriverinitiatedio.md) | The SetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |

    ## See Also

        <dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest3 interface%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>