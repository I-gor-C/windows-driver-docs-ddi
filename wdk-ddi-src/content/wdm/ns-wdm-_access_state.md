---
UID: NS.WDM._ACCESS_STATE
title: _ACCESS_STATE
author: windows-driver-content
description: The ACCESS_STATE structure describes the state of an access in progress.
old-location: ifsk\access_state.htm
old-project: ifsk
ms.assetid: 3d1d6407-f853-48d5-bd54-2eacece48b84
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _ACCESS_STATE, *PACCESS_STATE, ACCESS_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACCESS_STATE
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# _ACCESS_STATE structure



## -description
The ACCESS_STATE structure describes the state of an access in progress. It contains an object's subject context, remaining desired access types, granted access types, and, optionally, a privilege set to indicate which privileges were used to permit the access. 
Drivers are not to modify the ACCESS_STATE structure directly. To create and manipulate this structure, use the support routines listed in the See Also section. 


## -syntax

````
typedef struct _ACCESS_STATE {
  LUID                     OperationID;
  BOOLEAN                  SecurityEvaluated;
  BOOLEAN                  GenerateAudit;
  BOOLEAN                  GenerateOnClose;
  BOOLEAN                  PrivilegesAllocated;
  ULONG                    Flags;
  ACCESS_MASK              RemainingDesiredAccess;
  ACCESS_MASK              PreviouslyGrantedAccess;
  ACCESS_MASK              OriginalDesiredAccess;
  SECURITY_SUBJECT_CONTEXT SubjectSecurityContext;
  PSECURITY_DESCRIPTOR     SecurityDescriptor;
  PVOID                    AuxData;
  union {
    INITIAL_PRIVILEGE_SET InitialPrivilegeSet;
    PRIVILEGE_SET         PrivilegeSet;
  } Privileges;
  BOOLEAN                  AuditPrivileges;
  UNICODE_STRING           ObjectName;
  UNICODE_STRING           ObjectTypeName;
} ACCESS_STATE, *PACCESS_STATE;
````


## -struct-fields

### -field OperationID

The identifier of the operation that this access relates to. This member is replaced by TransactionId in the <b>AuxData</b> member and is currently unused by drivers. 

### -field SecurityEvaluated

A Boolean value that specifies whether security was evaluated as part of the access check. This member is currently unused by drivers. 

### -field GenerateAudit

A Boolean value that specifies whether the access should generate an audit. This member is currently unused by drivers. 

### -field GenerateOnClose

A Boolean value that specifies whether an audit should be generated when the handle being created is closed. This member is currently unused by drivers. 

### -field PrivilegesAllocated

A Boolean value that specifies whether privileges were allocated as part of the access check. This member is currently unused by drivers. 

### -field Flags

A 32-bit value that contains bit-field flags for the access. A driver can check for the traverse access flag (TOKEN_HAS_TRAVERSE_PRIVILEGE). For more information about how to check for traverse access, see <a href="ifsk.checking_for_traverse_privilege_on_irp_mj_create">Check for Traverse Privilege on IRP_MJ_CREATE</a>. A driver can also check for the TOKEN_IS_RESTRICTED flag. These flags are defined in Ntifs.h. 

### -field RemainingDesiredAccess

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> type that describes the access rights that have not yet been granted to the caller. A driver uses this member to determine if the Windows security system can grant access. If access can be granted, the driver updates the <b>PreviouslyGrantedAccess</b> and <b>RemainingDesiredAccess</b> members accordingly. 

### -field PreviouslyGrantedAccess

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> type that specifies the information about access that has already been granted to the caller of one of the <a href="ifsk.security_reference_monitor_routines">Security Reference Monitor Routines</a>. The Windows security system grants certain rights based on the privileges of the caller, such as traverse right (the ability to traverse through a directory as part of opening a subdirectory or file). 

### -field OriginalDesiredAccess

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> type that contains the original access rights that were requested by the caller. 

### -field SubjectSecurityContext

A <a href="ifsk.security_subject_context">SECURITY_SUBJECT_CONTEXT</a> structure that contains information about the subject security context that is used to validate and audit access. 

### -field SecurityDescriptor

A pointer to a <a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a> structure that contains security information for the object that this access relates to. 

### -field AuxData

A pointer to a memory block that contains auxiliary data for the access. 

### -field Privileges

A union that can contain one of the following structures. This union allows three privileges to be embedded in the access state structure. If any more privileges are required during the operation, they will be allocated in the <b>AuxData</b> member extension. This member is currently unused by drivers. 

### -field InitialPrivilegeSet

An <a href="ifsk.privilege_set">INITIAL_PRIVILEGE_SET</a> structure that specifies a set of initial privileges for the access. 

### -field PrivilegeSet

A <a href="ifsk.privilege_set">PRIVILEGE_SET</a> structure that specifies a set of privileges for the access. 
</dd>
</dl>

### -field AuditPrivileges

A Boolean value that specifies whether a privilege usage should be audited. This member is currently unused by drivers. 

### -field ObjectName

A <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the object name string for the access. This member is used for auditing. 

### -field ObjectTypeName

A <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the object type name string for the access. This member is used for auditing. 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="ifsk.irp_mj_create">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="ifsk.luid">LUID</a>
</dt>
<dt>
<a href="ifsk.obopenobjectbypointer">ObOpenObjectByPointer</a>
</dt>
<dt>
<a href="ifsk.privilege_set">PRIVILEGE_SET</a>
</dt>
<dt>
<a href="ifsk.seappendprivileges">SeAppendPrivileges</a>
</dt>
<dt>
<a href="ifsk.secapturesubjectcontext">SeCaptureSubjectContext</a>
</dt>
<dt>
<a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_subject_context">SECURITY_SUBJECT_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.seopenobjectauditalarm">SeOpenObjectAuditAlarm</a>
</dt>
<dt>
<a href="ifsk.seopenobjectfordeleteauditalarm">SeOpenObjectForDeleteAuditAlarm</a>
</dt>
<dt>
<a href="ifsk.sesetaccessstategenericmapping">SeSetAccessStateGenericMapping</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20ACCESS_STATE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
