---
UID: NS:wdm._IO_CONNECT_INTERRUPT_PARAMETERS
title: "_IO_CONNECT_INTERRUPT_PARAMETERS"
author: windows-driver-content
description: The IO_CONNECT_INTERRUPT_PARAMETERS structure contains the parameters that a driver supplies to the IoConnectInterruptEx routine to register an interrupt service routine (ISR).
old-location: kernel\io_connect_interrupt_parameters.htm
old-project: kernel
ms.assetid: 450c2e2b-56fa-4896-ba81-0f84f7e3051d
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: kstruct_b_c3854cf4-b084-42f4-9f3b-92a96fc741c1.xml, _IO_CONNECT_INTERRUPT_PARAMETERS, IO_CONNECT_INTERRUPT_PARAMETERS, kernel.io_connect_interrupt_parameters, wdm/IO_CONNECT_INTERRUPT_PARAMETERS, wdm/PIO_CONNECT_INTERRUPT_PARAMETERS, PIO_CONNECT_INTERRUPT_PARAMETERS structure pointer [Kernel-Mode Driver Architecture], PIO_CONNECT_INTERRUPT_PARAMETERS, *PIO_CONNECT_INTERRUPT_PARAMETERS, IO_CONNECT_INTERRUPT_PARAMETERS structure [Kernel-Mode Driver Architecture]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Wdm.h
apiname:
-	IO_CONNECT_INTERRUPT_PARAMETERS
product: Windows
targetos: Windows
req.typenames: "*PIO_CONNECT_INTERRUPT_PARAMETERS, IO_CONNECT_INTERRUPT_PARAMETERS"
req.product: Windows 10 or later.
---

# _IO_CONNECT_INTERRUPT_PARAMETERS structure
The <b>IO_CONNECT_INTERRUPT_PARAMETERS</b> structure contains the parameters that a driver supplies to the <a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a> routine to register an interrupt service routine (ISR).

## Syntax
````
typedef struct _IO_CONNECT_INTERRUPT_PARAMETERS {
  ULONG Version;
  union {
    struct {
      PDEVICE_OBJECT    PhysicalDeviceObject;
      PKINTERRUPT       *InterruptObject;
      PKSERVICE_ROUTINE ServiceRoutine;
      PVOID             ServiceContext;
      PKSPIN_LOCK       SpinLock;
      KIRQL             SynchronizeIrql;
      BOOLEAN           FloatingSave;
      BOOLEAN           ShareVector;
      ULONG             Vector;
      KIRQL             Irql;
      KINTERRUPT_MODE   InterruptMode;
      KAFFINITY         ProcessorEnableMask;
      USHORT            Group;
    } FullySpecified;
    struct {
      PDEVICE_OBJECT    PhysicalDeviceObject;
      PKINTERRUPT       *InterruptObject;
      PKSERVICE_ROUTINE ServiceRoutine;
      PVOID             ServiceContext;
      PKSPIN_LOCK       SpinLock;
      KIRQL             SynchronizeIrql;
      BOOLEAN           FloatingSave;
    } LineBased;
    struct {
      PDEVICE_OBJECT            PhysicalDeviceObject;
      union {
        PVOID                      *Generic;
        PIO_INTERRUPT_MESSAGE_INFO *InterruptMessageTable;
        PKINTERRUPT                *InterruptObject;
      } ConnectionContext;
      PKMESSAGE_SERVICE_ROUTINE MessageServiceRoutine;
      PVOID                     ServiceContext;
      PKSPIN_LOCK               SpinLock;
      KIRQL                     SynchronizeIrql;
      BOOLEAN                   FloatingSave;
      PKSERVICE_ROUTINE         FallBackServiceRoutine;
    } MessageBased;
  };
} IO_CONNECT_INTERRUPT_PARAMETERS, *PIO_CONNECT_INTERRUPT_PARAMETERS;
````

## Members


`Version`

On input, specifies the particular operation to be performed by <b>IoConnectInterruptEx</b>, as follows.
<table>
<tr>
<th>Version value</th>
<th>IoConnectInterruptEx operation</th>
</tr>
<tr>
<td>
CONNECT_FULLY_SPECIFIED

</td>
<td>
Connects to a specific interrupt using information provided by the Plug and Play (PnP) manager. Use the <b>FullySpecified</b> member to provide the additional parameters of the operation.

</td>
</tr>
<tr>
<td>
CONNECT_LINE_BASED

</td>
<td>
Registers an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547958">InterruptService</a> routine for the device's line-based interrupts. Use the <b>LineBased</b> member to provide the additional parameters of the operation.

</td>
</tr>
<tr>
<td>
CONNECT_MESSAGE_BASED

</td>
<td>
Registers an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547940">InterruptMessageService</a> routine for the device's message-signaled interrupts. The caller can also specify a fallback <i>InterruptService</i> routine if the device only has line-based interrupts. Use the <b>MessageBased</b> member to provide the additional parameters of the operation.

</td>
</tr>
</table> 

On return, the routine provides information about the operation, as follows.
<table>
<tr>
<th>Version value</th>
<th>Description</th>
</tr>
<tr>
<td>
CONNECT_FULLY_SPECIFIED

</td>
<td>
The caller specified CONNECT_LINE_BASED or CONNECT_MESSAGE_BASED for <b>Version</b> on a platform that does not support it. Retry the operation using CONNECT_FULLY_SPECIFIED.

</td>
</tr>
<tr>
<td>
CONNECT_LINE_BASED

</td>
<td>
The caller specified CONNECT_MESSAGE_BASED and the caller's fallback <i>InterruptService</i> routine was registered.

</td>
</tr>
<tr>
<td>
CONNECT_MESSAGE_BASED

</td>
<td>
The caller specified CONNECT_MESSAGE_BASED and the caller's <i>InterruptMessageService</i> routine was registered.

</td>
</tr>
</table>

## Remarks
The <a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a> routine takes a single <i>Parameters</i> parameter, which points to an <b>IO_CONNECT_INTERRUPT_PARAMETERS</b> structure that contains all of the parameters of the operation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_CONNECT_INTERRUPT_PARAMETERS structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>