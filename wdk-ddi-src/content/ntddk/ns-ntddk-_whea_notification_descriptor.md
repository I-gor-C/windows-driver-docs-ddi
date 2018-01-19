---
UID : NS:ntddk._WHEA_NOTIFICATION_DESCRIPTOR
title : _WHEA_NOTIFICATION_DESCRIPTOR
author : windows-driver-content
description : The WHEA_NOTIFICATION_DESCRIPTOR structure describes the notification mechanism that is used by an error source.
old-location : whea\whea_notification_descriptor.htm
old-project : whea
ms.assetid : 5b228bb8-dd31-484d-b87a-ec7fed433a4a
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_NOTIFICATION_DESCRIPTOR, *PWHEA_NOTIFICATION_DESCRIPTOR, WHEA_NOTIFICATION_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WHEA_NOTIFICATION_DESCRIPTOR
req.alt-loc : Ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PWHEA_NOTIFICATION_DESCRIPTOR, WHEA_NOTIFICATION_DESCRIPTOR"
---

# _WHEA_NOTIFICATION_DESCRIPTOR structure
The <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure describes the notification mechanism that is used by an error source.

## Syntax
````
struct WHEA_NOTIFICATION_DESCRIPTOR {
  UCHAR                   Type;
  UCHAR                   Length;
  WHEA_NOTIFICATION_FLAGS Flags;
  union {
    struct {
      ULONG PollInterval;
    } Polled;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Interrupt;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } LocalInterrupt;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Sci;
    struct {
      ULONG PollInterval;
      ULONG Vector;
      ULONG SwitchToPollingThreshold;
      ULONG SwitchToPollingWindow;
      ULONG ErrorThreshold;
      ULONG ErrorThresholdWindow;
    } Nmi;
  } u;
};
````

## Members

        
            `Flags`

            A WHEA_NOTIFICATION_FLAGS union that indicates which of the members of the <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure can be written to by the operating system. The WHEA_NOTIFICATION_FLAGS union is defined as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_NOTIFICATION_FLAGS {
  struct {
    USHORT  PollIntervalRW:1;
    USHORT  SwitchToPollingThresholdRW:1;
    USHORT  SwitchToPollingWindowRW:1;
    USHORT  ErrorThresholdRW:1;
    USHORT  ErrorThresholdWindowRW:1;
    USHORT  Reserved:11;
  };
  USHORT  AsUSHORT;
} WHEA_NOTIFICATION_FLAGS, *PWHEA_NOTIFICATION_FLAGS</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Length`

            The size, in bytes, of the <b>WHEA_NOTIFICATION_DESCRIPTOR</b> structure.
        
            `Type`

            The type of notification mechanism that is used by the error source. This can be one of the following possible values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `u`

            A union of structures that are specific to each different type of notification mechanism.

    ## Remarks
        A WHEA_NOTIFICATION_DESCRIPTOR structure is contained within the <a href="..\ntddk\ns-ntddk-_whea_generic_error_descriptor.md">WHEA_GENERIC_ERROR_DESCRIPTOR</a> and <a href="..\ntddk\ns-ntddk-_whea_xpf_cmc_descriptor.md">WHEA_XPF_CMC_DESCRIPTOR</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_generic_error_descriptor.md">WHEA_GENERIC_ERROR_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_cmc_descriptor.md">WHEA_XPF_CMC_DESCRIPTOR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_NOTIFICATION_DESCRIPTOR structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>