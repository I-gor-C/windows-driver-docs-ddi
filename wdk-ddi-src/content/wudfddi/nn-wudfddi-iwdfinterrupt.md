---
UID: NN:wudfddi.IWDFInterrupt
title: IWDFInterrupt
author: windows-driver-content
description: This interface exposes an interrupt object.
old-location: wdf\iwdfinterrupt.htm
old-project: wdf
ms.assetid: 729A2361-6FE1-4096-AC8B-3D042326EE5C
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: wdf.iwdfinterrupt, IWDFInterrupt interface, IWDFInterrupt interface, described, IWDFInterrupt, wudfddi/IWDFInterrupt, umdf.iwdfinterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	WUDFx.dll
apiname:
-	IWDFInterrupt
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFInterrupt interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

This interface exposes an interrupt object.

## Methods

<p>The <b>IWDFInterrupt</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFInterrupt.AcquireInterruptLock](nf-wudfddi-iwdfinterrupt-acquireinterruptlock.md) | The AcquireInterruptLock method begins a code sequence that executes while holding an interrupt object's lock. |
| [wudfddi.IWDFInterrupt.Disable](nf-wudfddi-iwdfinterrupt-disable.md) | The Disable method disables a specified device interrupt by calling the driver's OnInterruptDisable callback function. |
| [wudfddi.IWDFInterrupt.Enable](nf-wudfddi-iwdfinterrupt-enable.md) | The Enable method enables a specified device interrupt by calling the driver's OnInterruptEnable callback function. |
| [wudfddi.IWDFInterrupt.GetDevice](nf-wudfddi-iwdfinterrupt-getdevice.md) | The GetDevice method returns the framework device object interface for this interrupt object. |
| [wudfddi.IWDFInterrupt.GetInfo](nf-wudfddi-iwdfinterrupt-getinfo.md) | The GetInfo method retrieves information about a specified interrupt. |
| [wudfddi.IWDFInterrupt.QueueWorkItemForIsr](nf-wudfddi-iwdfinterrupt-queueworkitemforisr.md) | The QueueWorkItemForIsr method queues a work item to process interrupt-related work outside of the interrupt service routine. |
| [wudfddi.IWDFInterrupt.ReleaseInterruptLock](nf-wudfddi-iwdfinterrupt-releaseinterruptlock.md) | The ReleaseInterruptLock method ends a code sequence that executes while holding an interrupt object's lock. |
| [wudfddi.IWDFInterrupt.SetExtendedPolicy](nf-wudfddi-iwdfinterrupt-setextendedpolicy.md) | The SetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [wudfddi.IWDFInterrupt.SetPolicy](nf-wudfddi-iwdfinterrupt-setpolicy.md) | The SetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [wudfddi.IWDFInterrupt.TryToAcquireInterruptLock](nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock.md) | The TryToAcquireInterruptLock method acquires the interrupt lock if no other thread has already acquired it. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt interface%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>