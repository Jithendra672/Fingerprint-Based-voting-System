# Base class for biometric verification
class BiometricVerification:
    def verify_identity(self, biometric_data):
        """Abstract method to verify identity using biometric data."""
        raise NotImplementedError("This method should be overridden in derived classes.")

# Derived class for fingerprint verification
class FingerprintVerification(BiometricVerification):
    def verify_identity(self, fingerprint_data):
        """Verify identity using fingerprint data."""
        # Perform fingerprint matching logic
        print("Verifying fingerprint...")
        # Return True if the fingerprint matches, False otherwise
        return True

# Class representing a voter
class Voter:
    def __init__(self, voter_id, name, fingerprint_data):
        self.voter_id = voter_id
        self.name = name
        self.__fingerprint_data = fingerprint_data  # Private attribute
        self.has_voted = False
    
    def authenticate(self, verifier: BiometricVerification):
        """Authenticate voter using a biometric verifier."""
        return verifier.verify_identity(self.__fingerprint_data)
    
    def cast_vote(self):
        """Cast a vote if not already voted."""
        if not self.has_voted:
            print(f"Voter {self.name} is casting their vote...")
            self.has_voted = True
            return True
        else:
            print(f"Voter {self.name} has already voted.")
            return False

# Class representing the voting system
class VotingSystem:
    def __init__(self):
        self.voters = []
        self.verifier = FingerprintVerification()  # Using fingerprint verification

    def register_voter(self, voter_id, name, fingerprint_data):
        """Register a new voter."""
        voter = Voter(voter_id, name, fingerprint_data)
        self.voters.append(voter)

    def authenticate_voter(self, voter_id):
        """Authenticate voter based on their ID."""
        for voter in self.voters:
            if voter.voter_id == voter_id:
                return voter.authenticate(self.verifier)
        print("Voter not found!")
        return False

    def record_vote(self, voter_id):
        """Record the vote for an authenticated voter."""
        for voter in self.voters:
            if voter.voter_id == voter_id and voter.authenticate(self.verifier):
                return voter.cast_vote()
        print("Unable to record vote.")
        return False

# Example usage
voting_system = VotingSystem()
voting_system.register_voter(1, "Alice", "fingerprint_data_1")
voting_system.register_voter(2, "Bob", "fingerprint_data_2")

if voting_system.authenticate_voter(1):
    voting_system.record_vote(1)

if voting_system.authenticate_voter(2):
    voting_system.record_vote(2)
