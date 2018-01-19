---
UID : NS:ntifs.MARK_HANDLE_INFO32
title : MARK_HANDLE_INFO32
author : windows-driver-content
description : Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes.
old-location : ifsk\mark_handle_info32.htm
old-project : ifsk
ms.assetid : BAC97D72-23C4-49A6-A13D-0F011113DB32
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : MARK_HANDLE_INFO32, MARK_HANDLE_INFO32, *PMARK_HANDLE_INFO32
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Fltkernel.h, Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows XP.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MARK_HANDLE_INFO32
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : MARK_HANDLE_INFO32, *PMARK_HANDLE_INFO32
---

# MARK_HANDLE_INFO32 structure
Contains information that is used to mark a specified file or directory, and its update sequence 
    number (USN) change journal record with data about changes. This is only defined for 64-bit code and is used to 
    interpret input data formatted as a <a href="https://msdn.microsoft.com/6f736b31-279d-4118-a5e3-ad3c2bea2250">MARK_HANDLE_INFO</a> structure sent from 32-bit 
    code. It is used with the <a href="https://msdn.microsoft.com/c96b49d8-12f3-4281-9f9f-6621769359f0">FSCTL_MARK_HANDLE</a> 
    control code.

## Syntax
````
typedef struct {
#if (_WIN32_WINNT >= 0x0602)
  union {
    ULONG UsnSourceInfo;
    ULONG CopyNumber;
  };
#else 
  ULONG  UsnSourceInfo;
#endif 
  UINT32 VolumeHandle;
  ULONG  HandleInfo;
} MARK_HANDLE_INFO32, *PMARK_HANDLE_INFO32;
````

## Members

        
            `HandleInfo`

            The flag that specifies additional information about the file or directory identified by the handle value 
       in the <b>VolumeHandle</b> member.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `UsnSourceInfo`

            The type of changes being made.

The operation does not modify the file or directory externally from the point of view of the application that 
       created it.

When a thread writes a new USN record, the source information flags in the prior record continues to be 
       present only if the thread also sets those flags. Therefore, the source information structure allows 
       applications to filter out USN records that are set only by a known source, such as an antivirus filter.

The following values are defined.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `VolumeHandle`

            The volume handle to the volume where the file or directory resides. For more information on obtaining a 
        volume handle, see the Remarks section.

This handle is required to check the privileges for this operation.

The caller must have the <b>SE_MANAGE_VOLUME_NAME</b> privilege. For more information, 
        see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559863">Privileges</a>.

    ## Remarks
        When running on a 64-bit system, file system minifilters must interpret the input data sent by a 32-bit process in the system buffer for the <a href="https://msdn.microsoft.com/c96b49d8-12f3-4281-9f9f-6621769359f0">FSCTL_MARK_HANDLE</a> control code as a <b>MARK_HANDLE_INFO32</b> structure. A minifilter may check the process word length by calling <a href="..\fltkernel\nf-fltkernel-fltis32bitprocess.md">FltIs32bitProcess</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Fltkernel.h, Ntifs.h) |

    ## See Also

        <dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltis32bitprocess.md">FltIs32bitProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c96b49d8-12f3-4281-9f9f-6621769359f0">FSCTL_MARK_HANDLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6f736b31-279d-4118-a5e3-ad3c2bea2250">MARK_HANDLE_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MARK_HANDLE_INFO32 structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>