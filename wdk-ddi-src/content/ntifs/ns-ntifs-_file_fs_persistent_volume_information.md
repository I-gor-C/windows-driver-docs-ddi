---
UID : NS:ntifs._FILE_FS_PERSISTENT_VOLUME_INFORMATION
title : _FILE_FS_PERSISTENT_VOLUME_INFORMATION
author : windows-driver-content
description : The FILE_FS_PERSISTENT_VOLUME_INFORMATION structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer.
old-location : ifsk\file_fs_persistent_volume_information.htm
old-project : ifsk
ms.assetid : f1c7785e-e135-4060-8cf7-5c985b37ff83
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _FILE_FS_PERSISTENT_VOLUME_INFORMATION, *PFILE_FS_PERSISTENT_VOLUME_INFORMATION, FILE_FS_PERSISTENT_VOLUME_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows 7.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FILE_FS_PERSISTENT_VOLUME_INFORMATION
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
req.typenames : "*PFILE_FS_PERSISTENT_VOLUME_INFORMATION, FILE_FS_PERSISTENT_VOLUME_INFORMATION"
---

# _FILE_FS_PERSISTENT_VOLUME_INFORMATION structure
The <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer.

## Syntax
````
typedef struct _FILE_FS_PERSISTENT_VOLUME_INFORMATION {
  ULONG VolumeFlags;
  ULONG FlagMask;
  ULONG Version;
  ULONG Reserved;
} FILE_FS_PERSISTENT_VOLUME_INFORMATION, *PFILE_FS_PERSISTENT_VOLUME_INFORMATION;
````

## Members

        
            `FlagMask`

            A mask value for the valid flags that can appear in <b>VolumeFlags</b>. This is a bitwise OR combination of the desired flags described for <b>VolumeFlags</b>.
        
            `Reserved`

            Reserved. Set to 0;
        
            `Version`

            The version number of this structure. Set to 1.
        
            `VolumeFlags`

            The persistent state settings for a file system volume. This value is a bitwise OR combination of the following.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

    ## Remarks
        The <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545496">FSCTL_QUERY_PERSISTENT_VOLUME_STATE</a> control codes.

To query the state flags, <b>FlagMask</b> is set to a combination of flags to check for. For example, if the only the seek penalty flags are of interest, <b>FlagMask</b> = PERSISTENT_VOLUME_STATE_GLOBAL_METADATA_NO_SEEK_PENALTY | PERSISTENT_VOLUME_STATE_LOCAL_METADATA_NO_SEEK_PENALTY. Also, if only short name support is queried, then set <b>FlagMask</b> = PERSISTENT_VOLUME_STATE_SHORT_NAME_CREATION_DISABLED.

When setting or clearing the persistent volume state flags, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a>, <b>FlagMask</b> is set to all of the flags in <b>VolumeFlags</b> that will be affected for the volume. <b>VolumeFlags</b> contains the actual persistent state flags to set for the volume. The following example shows how to set the members of <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> to enable short name creation for a volume.

The <b>Version</b> member must be set to the current version of 1 for both a query and  a set  request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545496">FSCTL_QUERY_PERSISTENT_VOLUME_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_PERSISTENT_VOLUME_INFORMATION structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>